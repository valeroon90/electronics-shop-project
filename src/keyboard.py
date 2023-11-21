from src.item import Item

class MixinLang:

    def __init__(self, language="EN"):
        self.__language = language

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        if self.__language == "EN":
            self.__language = "RU"
        else:
            self.__language = "EN"
        return self


class Keyboard(Item, MixinLang):

    def __init__(self, name: str, price: float, quantity: int, language="EN"):
        super().__init__(name, price, quantity)
        self.__name = name
        MixinLang.__init__(self, language)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, data_str: str):
        self.__name = data_str


k = Keyboard('Dark Project KD87A', 10000, 8)