import pytest
from src.item import Item

object1 = Item("TV", 78000, 20)
item = Item('Телефон', 10000, 5)

def test_item():

    assert object1.price == 78000
    assert object1.calculate_total_price() == 1560000
    assert object1.apply_discount() == None
    Item.pay_rate = 0.5
    object1.apply_discount()
    assert object1.price == 39000

    #assert object1.name == "TV"
    item.name = 'Смартфон'
    assert item.name == 'Смартфон'

    item.name = "СуперСмартфон"
    assert item.name == "СуперСмартфон"

    item1 = Item.all[0]
    assert item1.name == 'TV'

    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5