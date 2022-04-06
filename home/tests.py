from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse


class HomePageTests(TestCase):

    """Test Homepage"""

    def setUp(self):
        pass

    def test_tilte_in_homepage(self):
        response = self.client.get(reverse('home:index'))
        self.assertContains(response, 'title')


    def test_body_in_homepage(self):
        response = self.client.get(reverse('home:index'))
        self.assertContains(response, 'id="contacts"')