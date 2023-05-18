from django.test import TestCase


# Create your tests here.
class TestCalc(TestCase):
    def test_endpoints(self):
        self.assertEquals(2, 3)
