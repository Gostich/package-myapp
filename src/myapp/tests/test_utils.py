from django.test import TestCase

from ..utils import format_hello


class TestUtils(TestCase):
    def test_format_hello(self):
        self.assertEqual(format_hello("world"), "Hello world")
