from django.test import TestCase
from rfix.task import models


class StateTest(TestCase):
    def setUp(self):
        self._objects = [
            ['closed', 'closed project'],
            ['opened', 'opened task']
        ]

        for object in self._objects:
            models.State.objects.create(name=object[0], description=object[1])

    def test_create(self):
        for object in self._objects:
            task_state = models.State.objects.get(name=object[0])
            self.assertEqual(task_state.name, object[0])
            self.assertEqual(task_state.description, object[1])
