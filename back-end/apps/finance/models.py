from django.db import models

from apps.common.models import TimeStampedModel


class Account(TimeStampedModel):
    class AccountType(models.TextChoices):
        CURRENT = "current_account", "Current account"
        SAVINGS = "savings_account", "Savings account"
        CASH_BOX = "cash_box", "Cash box"

    account_type = models.CharField(max_length=20, choices=AccountType.choices)
    name = models.CharField(max_length=255)
    balance = models.DecimalField(max_digits=16, decimal_places=0, default=0)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    @property
    def last_activity(self):
        latest = self.records.order_by("-date").first()
        return latest.date if latest else None


class FinanceRecord(TimeStampedModel):
    class RecordType(models.TextChoices):
        INCOME = "income", "Income"
        EXPENSE = "expense", "Expense"

    description = models.CharField(max_length=255)
    type = models.CharField(max_length=10, choices=RecordType.choices)
    category = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=14, decimal_places=0)
    date = models.DateField()
    account = models.ForeignKey(
        Account, on_delete=models.SET_NULL, null=True, blank=True, related_name="records"
    )

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        sign = "+" if self.type == self.RecordType.INCOME else "-"
        return f"{self.description} ({sign}{self.amount})"
