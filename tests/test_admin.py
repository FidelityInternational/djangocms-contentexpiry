from django.contrib.admin import site as admin_site
from django.test import TestCase, RequestFactory
from django.core.urlresolvers import reverse

from djangocms_contentexpiry.admin import ContentExpiryAdmin, ExpiryChangeList
from djangocms_contentexpiry.models import ContentExpiry

from .factories import PageContentExpiryFactory, TestModel1ExpiryFactory


class ModelAdminMethodTestCase(TestCase):

    def test_title(self):
        obj = PageContentExpiryFactory()
        title = ContentExpiryAdmin.title(None, obj)
        self.assertEqual(title, str(obj.content))


class ExpiryChangeListTestCase(TestCase):

    def _get_changelist(self):
        admin_class = admin_site._registry[ContentExpiry]
        return ExpiryChangeList(
            request=RequestFactory().get('/admin/'), model=ContentExpiry,
            list_display=('id',), list_display_links=('id',),
            list_filter=None, date_hierarchy=None, search_fields=None,
            list_select_related=None, list_per_page=100,
            list_max_show_all=200, list_editable=False,
            model_admin=admin_class)

    def test_admin_class_uses_custom_changelist_class(self):
        admin_class = admin_site._registry[ContentExpiry]
        changelist_class = admin_class.get_changelist(
            RequestFactory().get('/admin/'))
        self.assertEqual(changelist_class, ExpiryChangeList)

    def test_result_url_for_page_expiry(self):
        page_expiry = PageContentExpiryFactory()
        actual_url = self._get_changelist().url_for_result(page_expiry)
        expected_url = reverse(
            'admin:cms_pagecontent_change', args=(str(page_expiry.content.id)))
        self.assertEqual(actual_url, expected_url)

    def test_result_url_for_test_model1_expiry(self):
        model1_expiry = TestModel1ExpiryFactory()
        actual_url = self._get_changelist().url_for_result(model1_expiry)
        expected_url = reverse(
            'admin:app_1_testmodel1_change', args=(str(model1_expiry.content.id)))
        self.assertEqual(actual_url, expected_url)
