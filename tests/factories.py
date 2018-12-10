import string

from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType

import factory
from factory.fuzzy import FuzzyText

from djangocms_contentexpiry.models import ContentExpiry

from .content_factories import PageContentFactory, TestModel1Factory


class UserFactory(factory.django.DjangoModelFactory):
    username = FuzzyText(length=12)
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.LazyAttribute(
        lambda u: "%s.%s@example.com" % (u.first_name.lower(), u.last_name.lower()))

    class Meta:
        model = User


class AbstractContentExpiryFactory(factory.DjangoModelFactory):
    object_id = factory.SelfAttribute('content.id')
    content_type = factory.LazyAttribute(
        lambda o: ContentType.objects.get_for_model(o.content))
    modified_by = factory.SubFactory(UserFactory)

    class Meta:
        exclude = ['content']
        abstract = True


class PageContentExpiryFactory(AbstractContentExpiryFactory):
    content = factory.SubFactory(PageContentFactory)

    class Meta:
        model = ContentExpiry


class TestModel1ExpiryFactory(AbstractContentExpiryFactory):
    content = factory.SubFactory(TestModel1Factory)

    class Meta:
        model = ContentExpiry
