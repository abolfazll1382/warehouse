from django.db import transaction
from django.db.models import F

from apps.finance.models import Account, FinanceRecord


@transaction.atomic
def finance_record_create(
    *, description: str, type: str, category: str, amount: float, date, account: Account | None = None
) -> FinanceRecord:
    """
    Creates the record and, if it's tied to an account, keeps that account's
    balance in sync in the same transaction — so 'balance' is never allowed
    to drift out of step with the ledger of records that produced it.

    Uses an F() expression rather than read-balance-then-write-balance: the
    increment happens as a single atomic UPDATE in Postgres, so two
    concurrent postings can never race and silently drop one of them.
    """
    record = FinanceRecord.objects.create(
        description=description, type=type, category=category, amount=amount, date=date, account=account
    )

    if account is not None:
        delta = amount if type == FinanceRecord.RecordType.INCOME else -amount
        Account.objects.filter(pk=account.pk).update(balance=F("balance") + delta)

    return record
