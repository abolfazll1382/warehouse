# core/models.py

from django.db import models
from django.utils import timezone

class SoftDeleteManager(models.Manager):
    def get_queryset(self):
        # By default, only return objects that are NOT deleted
        return super().get_queryset().filter(is_deleted=False)

class SoftDeleteModel(models.Model):
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    # Use our custom manager as the default
    objects = SoftDeleteManager()
    # Keep the default manager around just in case we need to see deleted items (e.g., in Admin)
    all_objects = models.Manager() 

    class Meta:
        abstract = True # This tells Django NOT to create a database table for this specific class

    def delete(self, *args, **kwargs):
        """
        Override the default delete method to soft-delete instead.
        """
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()