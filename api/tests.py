from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Task


class HelloEndpointTests(APITestCase):
    def test_hello_returns_200(self):
        response = self.client.get(reverse("hello"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_hello_returns_message(self):
        response = self.client.get(reverse("hello"))
        self.assertEqual(response.data["message"], "Hello from CSC325!")
        self.assertEqual(response.data["status"], "ok")


class TaskEndpointTests(APITestCase):
    def test_create_task(self):
        response = self.client.post("/api/tasks/", {"title": "Write tests"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
        self.assertFalse(response.data["done"])

    def test_list_tasks(self):
        Task.objects.create(title="First")
        Task.objects.create(title="Second")
        response = self.client.get("/api/tasks/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_task_without_title_fails(self):
        response = self.client.post("/api/tasks/", {}, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
