from rfix.utils.test import Tests
from rfix.project import models


class ProjectViewTest(Tests.AbsoluteUrl):
    def make_object(self):
        return models.Project.objects.create(
            slug='project',
            name='Test project',
            description='Test project description'
        )

    def login(self):
        Tests.make_user()
        self._client.login(username='user', password='password')
