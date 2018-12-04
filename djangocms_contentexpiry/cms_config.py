from collections import Iterable

from django.core.exceptions import ImproperlyConfigured

from cms.app_base import CMSAppConfig, CMSAppExtension


class ContentExpiryCMSExtension(CMSAppExtension):

    def __init__(self):
        self.contentexpiry_apps_models = []

    def configure_app(self, cms_config):
        if hasattr(cms_config, 'contentexpiry_models'):
            contentexpiry_app_models = getattr(cms_config, 'contentexpiry_models')
            if isinstance(contentexpiry_app_models, Iterable):
                self.contentexpiry_apps_models.extend(contentexpiry_app_models)
            else:
                raise ImproperlyConfigured(
                    "ContentExpiry configuration must be a Iterable object")
        else:
            raise ImproperlyConfigured(
                "cms_config.py must have contentexpiry_models attribute")


class CoreCMSAppConfig(CMSAppConfig):
    djangocms_contentexpiry_enabled = True
    contentexpiry_models = []
