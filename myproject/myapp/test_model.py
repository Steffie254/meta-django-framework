from django.test import TestCase
from .models import Drinks, DrinksCategory

class DrinksModelTest(TestCase):

    def setUp(self):
        # Create a DrinksCategory instance
        self.category = DrinksCategory.objects.create(name="Soft Drink")

        # Create a Drinks instance
        self.drink = Drinks.objects.create(
            drink="Cola",
            price=2,
            category_id=self.category
        )

    def test_drinks_creation(self):
        # Ensure the drink instance is created correctly
        self.assertEqual(self.drink.drink, "Cola")
        self.assertEqual(self.drink.price, 2)
        self.assertEqual(self.drink.category_id.name, "Soft Drink")

    def test_string_representation(self):
        # Ensure the string representation is correct if you have defined __str__ method
        self.assertEqual(str(self.drink), self.drink.drink)

    def test_category_relationship(self):
        # Ensure the relationship with category is correct
        self.assertEqual(self.drink.category_id, self.category)
