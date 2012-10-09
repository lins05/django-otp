from unittest import skipIf

import django
from django.contrib.auth.models import User
from django.test import TestCase


@skipIf(django.VERSION < (1,4), 'Requires Django 1.4')
class OTPAgentsTestCase(TestCase):
    fixtures = ['test/alice.yaml']
    urls = 'otp_agents.tests.urls'

    def setUp(self):
        self.alice = User.objects.get()

    def test_otp_anonymous(self):
        response = self.client.get('/otp/')

        self.assertEquals(response.status_code, 302)

    def test_otp_aythenticated(self):
        self.login()
        response = self.client.get('/otp/')

        self.assertEquals(response.status_code, 302)

    def test_otp_verified(self):
        self.verify()
        response = self.client.get('/otp/')

        self.assertEquals(response.status_code, 200)

    def test_otp_trusted(self):
        self.trust(True)
        self.logout()
        self.login()
        response = self.client.get('/otp/')

        self.assertEquals(response.status_code, 302)

    def test_otp2_verified(self):
        self.verify()
        response = self.client.get('/otp2/')

        self.assertEquals(response.status_code, 200)

    def test_agent_anonymous(self):
        response = self.client.get('/agent/')

        self.assertEquals(response.status_code, 302)

    def test_agent_authenticated(self):
        response = self.client.get('/agent/')

        self.assertEquals(response.status_code, 302)

    def test_agent_verified(self):
        self.verify()
        response = self.client.get('/agent/')

        self.assertEquals(response.status_code, 200)

    def test_agent_trusted_session(self):
        self.trust(False)
        response = self.client.get('/agent/')

        self.assertEquals(response.status_code, 200)

    def test_agent_trusted(self):
        self.trust(True)
        self.logout()
        self.login()
        response = self.client.get('/agent/')

        self.assertEquals(response.status_code, 200)

    def test_two_step_trust(self):
        self.login()
        self.add_trust(True)
        self.logout()
        self.login()
        response = self.client.get('/agent/')

        self.assertEquals(response.status_code, 200)


    def login(self):
        params = {
            'username': 'alice',
            'password': 'alice',
        }

        response = self.client.post('/login/', params)

        self.assertEquals(response.status_code, 302)

    def verify(self):
        params = {
            'username': 'alice',
            'password': 'alice',
            'otp_token': 'alice1',
        }

        response = self.client.post('/verify/', params)

        self.assertEquals(response.status_code, 302)

    def trust(self, persist=False):
        params = {
            'username': 'alice',
            'password': 'alice',
            'otp_token': 'alice1',
            'otp_trust_agent': '1' if persist else '',
        }

        response = self.client.post('/trust/', params)

        self.assertEquals(response.status_code, 302)

    def add_trust(self, persist=False):
        params = {
            'otp_device': 'django_otp.plugins.otp_static.models.StaticDevice/1',
            'otp_token': 'alice1',
            'otp_trust_agent': '1' if persist else '',
        }

        response = self.client.post('/trust/', params)

        self.assertEquals(response.status_code, 302)

    def logout(self):
        response = self.client.post('/logout/')

        self.assertEquals(response.status_code, 200)
