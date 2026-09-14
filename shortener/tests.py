from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import URL

class URLShortenerTests(APITestCase):
    def test_create_short_url(self):
        url = reverse('shorten-url')
        data = {'original_url': 'https://www.google.com'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('short_code', response.data)
        self.assertEqual(URL.objects.count(), 1)

    def test_redirect_url(self):
        obj = URL.objects.create(original_url='https://www.google.com')
        url = reverse('redirect-url', kwargs={'short_code': obj.short_code})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(response.url, 'https://www.google.com')
        obj.refresh_from_db()
        self.assertEqual(obj.clicks_count, 1)
