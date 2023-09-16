import pytest
from src.item import Item

object1 = Item("TV", 78000, 20)

def test_item():
    assert object1.name == "TV"
    assert object1.price == 78000
    assert object1.calculate_total_price() == 1560000
   #assert object1.apply_discount() == None
    Item.pay_rate = 0.5
    object1.apply_discount()
    assert object1.price == 39000