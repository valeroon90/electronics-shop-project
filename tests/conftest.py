import pytest
from src.item import Item
from src.phone import Phone
from src.keyboard import Keyboard

@pytest.fixture
def object1():
    return Item("Суперпуперск", 78000, 10)


@pytest.fixture
def object2():
    return Phone("OnePlus_7T", 55000, 20, 2)


@pytest.fixture
def object3():
    return Keyboard("BLOODY PUNK B810RC", 5100, 20)
