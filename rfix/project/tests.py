from django.test import TestCase
from django.test import Client
from rfix.project import models


class ProjectViewTest(TestCase):
    def setUp(self):
        self._slug = 'project'
        self._project = models.Project.objects.create(
            slug=self._slug,
            name='Test project',
            description='Test project description'
        )
        self._client = Client()

    def test_detail_url(self):
        res = self._client.get(self._project.get_absolute_url())
        self.assertEqual(res.status_code, 200)
