from binascii import unhexlify
from time import time

from django.test import TestCase

from .models import HOTPDevice, TOTPDevice


class HOTPTest(TestCase):
    fixtures = ['tests/oath']

    key = unhexlify('d2e8a68036f68960b1c30532bb6c56da5934d879')
    tokens = [782373, 313268, 307722]

    def setUp(self):
        self.device = HOTPDevice.objects.get()

    def test_normal(self):
        ok = self.device.verify_token(self.tokens[0])

        self.assert_(ok)
        self.assertEqual(self.device.counter, 1)

    def test_normal_drift(self):
        ok = self.device.verify_token(self.tokens[1])

        self.assert_(ok)
        self.assertEqual(self.device.counter, 2)

    def test_excessive_drift(self):
        ok = self.device.verify_token(self.tokens[2])

        self.assert_(not ok)
        self.assertEqual(self.device.counter, 0)

    def test_bad_value(self):
        ok = self.device.verify_token(123456)

        self.assert_(not ok)
        self.assertEqual(self.device.counter, 0)


class TOTPTest(TestCase):
    fixtures = ['tests/oath']

    key = unhexlify('2a2bbba1092ffdd25a328ad1a0a5f5d61d7aacc4')
    tokens = [179225, 656163, 839400, 346912]

    def setUp(self):
        """
        Load the device and move it to the third time step.
        """
        self.device = TOTPDevice.objects.get()
        self.device.t0 = int(time() - 60)

    def test_current(self):
        ok = self.device.verify_token(self.tokens[2])

        self.assert_(ok)

    def test_previous(self):
        ok = self.device.verify_token(self.tokens[1])

        self.assert_(ok)

    def test_past(self):
        ok = self.device.verify_token(self.tokens[0])

        self.assert_(not ok)

    def test_future(self):
        ok = self.device.verify_token(self.tokens[3])

        self.assert_(not ok)
