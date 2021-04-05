from django.test import TestCase
from django.urls import reverse

class SimpleTextCase(SimpleTextCase):
    def text_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

class ViewsTestCase(TestCase):
	# utiliza el cliente de prueba de Django para visitar la página principal del sitio web
    def test_index_loads_properly(self):
        response = self.client.get('your_server_ip:8000')
        self.assertEqual(response.status_code, 200)

class SimpleTextCase2(SimpleTextCase):
    def text_about_page_status_code(self):
        response = self.client.get(reverse.('about'))
        self.assertEqual(response.status_code, 200)