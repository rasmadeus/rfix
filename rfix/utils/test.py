from __future__ import unicode_literals
from abc import ABCMeta
from abc import abstractmethod
from django.test import TestCase
from django.test import Client
from rfix.rfixuser.models import RfixUser


class Tests:
    @staticmethod
    def make_user(username='user', password='password'):
        user = RfixUser.objects.create(
            slug='user',
            username=username,
            email='user@user.com',
            photo='user.png'
        )
        user.set_password(password)
        user.save()
        return user

    class AbsoluteUrl(TestCase):
        __metaclass__ = ABCMeta

        @abstractmethod
        def make_object(self):
            pass

        @abstractmethod
        def login(self):
            pass

        def setUp(self):
            self._client = Client()
            self._object = self.make_object()
            self._object.save()

        def test_absolute_url(self):
            self.login()
            res = self._client.get(self._object.get_absolute_url())
            self.assertEqual(res.status_code, 200)
