from unittest import TestCase
from convert import converter

class convert_test(TestCase):
    def test_converter(self):
            self.assertEqual(converter('USD', 'USD', 1), 1)