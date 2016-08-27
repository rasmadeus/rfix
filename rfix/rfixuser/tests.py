from rfix.utils.test import Tests


class RfixUserViewTest(Tests.AbsoluteUrl):
    def make_object(self):
        return Tests.make_user()

    def login(self):
        self._client.login(username='user', password='password')
