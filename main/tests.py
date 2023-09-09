from django.test import TestCase, Client
from main.models import Item

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')
    
    def setUp(self):
        Item.objects.create(name="Obsidian",amount="64",
                            description="Obsidian is a block found naturally in all dimensions, and created when water flows over a lava source.")
        Item.objects.create(name="Diamond",amount="32",
                            description="A diamond is a mineral that can only be obtained from diamond ore, loot chests and suspicious blocks.")
        
    def test_items_can_created(self):
        obsidian = Item.objects.get(name="Obsidian")
        diamond = Item.objects.get(name="Diamond")
        self.assertEqual(obsidian.name, "Obsidian")
        self.assertEqual(diamond.name, "Diamond")
        self.assertEqual(obsidian.amount, 64)
        self.assertEqual(diamond.amount, 32)

# Source
# 1. https://docs.djangoproject.com/en/4.2/topics/testing/overview/
# 2. https://minecraft.fandom.com/wiki/


    