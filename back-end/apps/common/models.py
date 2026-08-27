from django.db import models


class TimeStampedModel(models.Model):
    """
    Abstract base — every domain model inherits this instead of redeclaring
    created_at/updated_at. Keeps audit fields consistent across all 7 apps.
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
