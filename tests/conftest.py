import pytest
from src.item import Item


@pytest.fixture
def object1():
    return Item("Суперпуперск", 78000, 10)

