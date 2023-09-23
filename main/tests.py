from django.test import TestCase, Client
from main.models import Item

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/login/')
        self.assertEqual(response.status_code, 200)
    

# Source
# 1. https://docs.djangoproject.com/en/4.2/topics/testing/overview/
# 2. https://minecraft.fandom.com/wiki/


    