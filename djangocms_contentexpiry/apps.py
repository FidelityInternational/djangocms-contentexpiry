from __future__ import unicode_literals

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ContentexpiryConfig(AppConfig):
    name = 'djangocms_contentexpiry'
    verbose_name = _('django CMS Content expiry')
