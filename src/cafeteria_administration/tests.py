from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from cafeteria_administration.views import cafeteria
from django.template.loader import render_to_string


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/cafeteria/')
        self.assertEqual(found.func, cafeteria)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = cafeteria(request)
        expected_html = render_to_string('cafeteria.html')
        self.assertEqual(response.content.decode(), expected_html)
