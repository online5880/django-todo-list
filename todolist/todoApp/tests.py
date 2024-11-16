from django.test import TestCase

# Create your tests here.
from .models import Task
from django.contrib.auth.models import User
from django.urls import reverse


class TaskModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password")
        self.task = Task.objects.create(
            user=self.user,  # user를 명시적으로 추가
            title="Test Task",
            description="This is a test task.",
            completed=False,
        )

    def test_task_creation(self):
        self.assertEqual(self.task.title, "Test Task")
        self.assertEqual(self.task.user, self.user)  # user와 연결 확인
        self.assertFalse(self.task.completed)

    def test_task_str_representation(self):
        self.assertEqual(str(self.task), "Test Task")
        
        
class TaskViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password")
        self.task = Task.objects.create(
            user=self.user,  # user 필드 추가
            title="Test Task",
            description="Description",
            completed=False,
        )

    def test_task_list_view(self):
        self.client.login(username="testuser", password="password")  # 로그인
        response = self.client.get(reverse('task_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Task")

    def test_task_create_view(self):
        self.client.login(username="testuser", password="password")  # 로그인
        response = self.client.post(reverse('task_create'), {
            'user': self.user.id,  # user 필드 추가
            'title': 'New Task',
            'description': 'New Description',
            'completed': False,
        })
        self.assertEqual(response.status_code, 302)  # Redirect after creation
        self.assertEqual(Task.objects.last().title, "New Task")