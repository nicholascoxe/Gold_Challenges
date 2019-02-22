
class Item:

    def __init__(self, number, name, ingredients, price, description):
        self.number = number
        self.name = name
        self.ingredients = ingredients
        self.price = price
        self.description = description
    def __repr__(self):
        return self.name