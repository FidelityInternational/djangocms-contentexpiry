from datetime import datetime, timedelta

from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import ugettext_lazy as _


class ContentExpiry(models.Model):
    activation_date = models.DateTimeField(auto_now_add=True)
    expiry_date = models.DateTimeField(
        default=datetime.now() + timedelta(days=30)
    )
    modified_by =  models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        verbose_name=_('author')
    )
    modified_on = models.DateTimeField(auto_now=True)
    content = GenericForeignKey('content_type', 'object_id')
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.PROTECT,
    )
    object_id = models.PositiveIntegerField()

    class Meta:
        unique_together = ("content_type", "object_id")
