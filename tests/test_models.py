from django.test import TestCase

from .factories import PageContentExpiryFactory


class ModelTestCase(TestCase):

    def test_str(self):
        expiry = PageContentExpiryFactory()
        self.assertEqual(str(expiry), str(expiry.content))
