from django.test import TestCase
from django.test import RequestFactory
from django.test import Client
from rfix.rfixuser import models
from rfix.rfixuser import views


class RfixUserViewTest(TestCase):
    def setUp(self):
        self._slug = 'user'
        self._user = models.RfixUser.objects.create(
            username=self._slug,
            email='user@user.com',
            password='password',
            slug=self._slug,
            photo='user.png'
        )
        self._factory = RequestFactory()
        self._client = Client()

    def test_detail(self):
        req = self._factory.get('/users/')
        res = views.RfixUserDetail.as_view()(req, slug=self._slug)
        self.assertEqual(res.status_code, 200)

    def test_detail_url(self):
        res = self._client.get('/users/{slug}/'.format(slug=self._slug))
        self.assertEqual(res.status_code, 200)
