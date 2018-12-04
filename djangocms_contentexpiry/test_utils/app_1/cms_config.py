from cms.app_base import CMSAppConfig
from .models import TestModel1, TestModel2

class CMSApp1Config(CMSAppConfig):
    djangocms_contentexpiry_enabled = True
    contentexpiry_models = [TestModel1, TestModel2]
