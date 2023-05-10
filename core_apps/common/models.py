from django.db import models
from django.db import models
from django.core.exceptions import ObjectDoesNotExist
import uuid


class AbstractManager(models.Manager):
    def get_object_by_public_id(self, id):
        try:
            instance = self.get(id=id)
            return instance
        except (ObjectDoesNotExist, ValueError, TypeError):
            raise ValueError(_("ID Cannot be found"))

class TimeStampedUUIDModel(models.Model):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = AbstractManager()

    class Meta:
        abstract = True
        ordering = ["-created_at", "-updated_at"]
        get_latest_by = 'created_at'