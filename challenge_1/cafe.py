
import item

items = []


def add_item(number, name, ingredients, price, description):
    i = item.Item(number, name, ingredients, price, description)
    items.append(i)


def get_items():
    return items


def delete_item(name):
    for item in items:
        if name == item.name:
            index = items.index(item)
            del items[index]
            return True
        