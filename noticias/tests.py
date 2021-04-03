from django.test import TestCase
from django.urls import reverse

class SimpleTextCase(SimpleTextCase):
    def text_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    def text_about_page_status_code(self):
        response = self.client.get(reverse.('about'))
        self.assertEqual(response.status_code, 200)