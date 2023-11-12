from src.item import Item
from src.phone import Phone


def test_calculate_total_price(object1):
    assert object1.calculate_total_price() == 780000


def test_apply_discount_with_pay_rate(object1):
    Item.pay_rate = 0.5
    assert Item.apply_discount(object1) == 39000


def test_apply_discount(object1):
    Item.pay_rate = 1
    assert Item.apply_discount(object1) == 78000


def test_name():
    object1 = Item("TV", 78000, 20)
    assert object1.name == "TV"
    object1.name = 'СуперСмартфон'
    assert object1.name == 'СуперСмарт'


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test__repr__(object1):
    assert repr(object1) == "Item('Суперпупер', 78000, 10)"


def test__str__(object1):
    assert str(object1) == 'Суперпупер'


def test__add__():
    phone1 = Phone("iPhone 14", 120000, 5, 2)
    item1 = Item("Смартфон", 10000, 20)
    assert item1 + phone1 == 25
