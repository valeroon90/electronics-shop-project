def test__repr__(object2):
    assert repr(object2) == "Phone('OnePlus_7T', 55000, 20, 2)"


def test__str__(object2):
    assert str(object2) == 'OnePlus_7T'


def test_number_of_sim(object2):
    assert object2.number_of_sim == 2


def test__add__(object2):
    assert object2 + object2 == 40