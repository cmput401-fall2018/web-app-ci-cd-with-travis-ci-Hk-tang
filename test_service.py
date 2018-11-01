from unittest import TestCase
from unittest.mock import patch
from service import Service


class TestService(TestCase):
    @patch('service.Service.bad_random', return_value=10)
    def test_bad_random(self, bad_random):
        service = Service()
        self.assertEqual(service.bad_random(), 10)

    @patch('service.Service.bad_random', return_value=10)
    def test_divide(self, bad_random):
        service = Service()
        self.assertEqual(service.divide(5), 2)
        self.assertEqual(service.divide(-2), -5)
        self.assertEqual(service.divide(1000000), 10e-6)
        try:
            service.divide(0)
            self.assertTrue(True)
        except Exception as e:
            self.assertEqual(e.__class__, ZeroDivisionError)
        try:
            service.divide("hello")
            self.assertTrue(True)
        except Exception as e:
            self.assertEqual(e.__class__, TypeError)

    def test_abs(self):
        service = Service()
        self.assertEqual(service.abs_plus(-5), 6)
        self.assertEqual(service.abs_plus(10000000), 10000001)
        self.assertEqual(service.abs_plus(0), 1)
        try:
            service.abs_plus("hello")
            self.assertTrue(True)
        except Exception as e:
            self.assertEqual(e.__class__, TypeError)

    @patch('service.Service.bad_random', return_value=10)
    def test_complicated_function(self, bad_random):
        service = Service()
        div, rando = service.complicated_function(10)
        self.assertEqual(div, 1)
        self.assertEqual(rando, 0)