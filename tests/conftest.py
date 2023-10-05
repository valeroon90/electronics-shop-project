import pytest
from src.item import Item


@pytest.fixture
def object1():
    return Item("TV", 78000, 20)


