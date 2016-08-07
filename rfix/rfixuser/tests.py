from django.test import TestCase
from django.test import RequestFactory
from django.test import Client
from rfix.rfixuser import models


class RfixUserViewTest(TestCase):
    def setUp(self):
        self._slug = 'user'
        self._user_password = 'password'
        self._user = models.RfixUser.objects.create(
            username='user',
            email='user@user.com',
            slug=self._slug,
            photo='user.png'
        )
        self._user.set_password('password')
        self._user.save()
        self._factory = RequestFactory()
        self._client = Client()

    def test_detail_url(self):
        self._client.login(
            username=self._user.username,
            password=self._user_password
        )
        res = self._client.get(self._user.get_absolute_url())
        self.assertEqual(res.status_code, 200)
