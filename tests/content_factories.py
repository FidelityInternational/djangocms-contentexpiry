import string

from django.contrib.sites.models import Site

import factory
from factory.fuzzy import FuzzyText, FuzzyChoice, FuzzyInteger

from cms.models import Page, PageContent, Placeholder, TreeNode

from djangocms_contentexpiry.test_utils.app_1.models import TestModel1


class TreeNodeFactory(factory.django.DjangoModelFactory):
    site = factory.fuzzy.FuzzyChoice(Site.objects.all())
    depth = 0
    # NOTE: Generating path this way is probably not a good way of
    # doing it, but seems to work for our present tests which only
    # really need a tree node to exist and not throw unique constraint
    # errors on this field. If the data in this model starts mattering
    # in our tests then something more will need to be done here.
    path = FuzzyText(length=8, chars=string.digits)

    class Meta:
        model = TreeNode


class PageFactory(factory.django.DjangoModelFactory):
    node = factory.SubFactory(TreeNodeFactory)

    class Meta:
        model = Page


class PageContentFactory(factory.django.DjangoModelFactory):
    page = factory.SubFactory(PageFactory)
    language = FuzzyChoice(['en', 'fr', 'it'])
    title = FuzzyText(length=12)
    page_title = FuzzyText(length=12)
    menu_title = FuzzyText(length=12)
    meta_description = FuzzyText(length=12)
    redirect = FuzzyText(length=12)
    created_by = FuzzyText(length=12)
    changed_by = FuzzyText(length=12)
    in_navigation = FuzzyChoice([True, False])
    soft_root = FuzzyChoice([True, False])
    template = FuzzyText(length=12)
    limit_visibility_in_menu = FuzzyInteger(0, 25)
    xframe_options = FuzzyInteger(0, 25)

    class Meta:
        model = PageContent


class TestModel1Factory(factory.django.DjangoModelFactory):

    class Meta:
        model = TestModel1
