from src.keyboard import MixinLang
from src.keyboard import Keyboard
import pytest


def test__str__(object3):
    assert str(object3) == "BLOODY PUNK B810RC"


def test_language(object3):
    assert str(object3.language) == "EN"


def test_change_lang(object3):
    object3.change_lang()
    assert str(object3.language) == "RU"
    object3.change_lang().change_lang()
    assert str(object3.language) == "RU"