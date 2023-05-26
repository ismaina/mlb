from django.db import models
from core_apps.common.models import TimeStampedUUIDModel
from django.urls import reverse
from core_apps.common.utils import upload_image_path
import uuid

class Contact(TimeStampedUUIDModel):
    uuid = models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    message = models.TextField(blank=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    image = models.ImageField(upload_to=upload_image_path, blank=True, null=True)
    supported = models.BooleanField(default=False)
    email = models.EmailField()

    class Meta:
        verbose_name_plural = 'contacts'

    @property
    def full_name(self):
        return u'%s %s' % (self.first_name, self.last_name)
    
    def __unicode__(self):
        return u'%s' % self.full_name
