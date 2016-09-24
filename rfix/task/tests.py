from rfix.utils.test import Tests
from rfix.project.models import Project
from rfix.task import models


class TaskDetailTest(Tests.AbsoluteUrl):
    def make_object(self):
        user = Tests.make_user()

        project = Project.objects.create(
            slug='project',
            name='Test project',
            description='Test project',
        )

        return models.Task.objects.create(
            name='Test task',
            description='Test task',
            project=project,
            performer=user
        )

    def login(self):
        self._client.login(username='user', password='password')
