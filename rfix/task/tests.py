from django.test import TestCase
from rfix.taskstate.models import State


class StateTest(TestCase):
    def setUp(self):
        self._objects = [['closed', 'closed project'], ['opened', 'opened task']]

        for object in self._objects:
            TaskState.objects.create(name=object[0], description=object[1])


    def test_create(self):
        for object in self._objects:
            task_state = TaskState.objects.get(name=object[0])
            self.assertEqual(task_state.name, object[0])
            self.assertEqual(task_state.description, object[1])
