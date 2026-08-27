from apps.finance.models import Account, FinanceRecord


def account_list():
    return Account.objects.all()


def finance_record_list(*, type: str | None = None, account_id: int | None = None):
    qs = FinanceRecord.objects.select_related("account")
    if type:
        qs = qs.filter(type=type)
    if account_id:
        qs = qs.filter(account_id=account_id)
    return qs
