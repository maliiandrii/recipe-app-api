"""
Tests for the health check.
"""
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient


class HealthCheckTests(TestCase):
    """Test health check."""

    def test_health_check(self):
        """Test health check."""
        client = APIClient()
        url = reverse('health-check')
        response = client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
