from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from apps.common.models import TimeStampedModel


class ProductionLine(TimeStampedModel):
    class Status(models.TextChoices):
        ACTIVE = "active", "Active"
        INACTIVE = "inactive", "Inactive"
        PROCESSING = "processing", "Processing"

    name = models.CharField(max_length=150)
    product = models.CharField(max_length=255)
    capacity = models.CharField(max_length=50, help_text="Free-form, e.g. '42 tons/day'.")
    efficiency = models.PositiveSmallIntegerField(
        default=0, validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    status = models.CharField(max_length=12, choices=Status.choices, default=Status.ACTIVE)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class QualityCheck(TimeStampedModel):
    class Result(models.TextChoices):
        PASSED = "passed", "Passed"
        FAILED = "failed", "Failed"
        REVIEW = "review", "Needs review"

    line = models.ForeignKey(
        ProductionLine, on_delete=models.SET_NULL, null=True, blank=True, related_name="quality_checks"
    )
    product = models.CharField(max_length=255)
    date = models.DateField()
    inspector = models.ForeignKey(
        "hr.Employee", on_delete=models.SET_NULL, null=True, related_name="quality_checks"
    )
    result = models.CharField(max_length=10, choices=Result.choices, default=Result.REVIEW)
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return f"{self.product} — {self.get_result_display()} ({self.date})"
