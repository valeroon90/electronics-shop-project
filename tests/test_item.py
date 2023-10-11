import pytest
from src.item import Item


def test_calculate_total_price(object1):
    assert object1.calculate_total_price() == 780000


def test_apply_discount_with_pay_rate(object1):
    Item.pay_rate = 0.5
    assert object1.apply_discount() == 39000


def test_apply_discount(object1):
    Item.pay_rate = 1
    assert object1.apply_discount() == 78000


def test_name(object1):
    #object2 = Item("TVV", 30000, 10)
    #assert object2.name == "TVV"
    assert object1.name == 'Суперпупер'


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test___repr__(object1):
    assert repr(object1) == "Item('Суперпупер', 78000, 10)"


def test__str__(object1):
    assert str(object1) == 'Суперпупер'

