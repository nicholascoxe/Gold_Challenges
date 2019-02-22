
import unittest
import cafe

class TestCafe(unittest.TestCase):
    
    def test_cafe_add_item_should(self):
        # arrange
        self.number = 'number'
        self.name = 'name'
        self.ingredients = 'ingredients'
        self.price = 'price'
        self.description = 'description'
        
        # act
        cafe.add_item(self.number, self.name, self.ingredients, self.price, self.description)
        actual = len(cafe.items)
        expected = 1

        # assert
        self.assertEqual(actual, expected)

    def test_cafe_get_items_should_be_equal(self):
        # act
        actual = len(cafe.get_items())
        expected = 1
        # assert
        self.assertEqual(actual, expected)

    def test_cafe_delete_item_should_delete_item(self):
        self.name = 'name'

        cafe.add_item(self.number, self.name, self.ingredients, self.price, self.description)
        self.assertTrue(cafe.delete_item(self.name))
