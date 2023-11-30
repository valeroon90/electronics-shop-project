import csv
#from abc import ABC, abstractmethod

class InstantiateCSVError(Exception):
    pass


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name[:10]
        self.price = price
        self.quantity = quantity
        self.total_price = self.quantity * self.price
        Item.all.append(self)
        #super().__init__()


    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.name}"

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        else:
            raise ValueError("Нельзя сложить `Phone` или `Item` с экземплярами не `Phone` или `Item` классов")

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self):
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate
        return self.price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, data_str: str):
        self.__name = data_str[:10]

    @classmethod
    def instantiate_from_csv(cls):
        try:
            Item.all = []
            with open('..\src\items.csv', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if 'name' not in row or 'price' not in row or 'quantity' not in row:
                        raise InstantiateCSVError
                    cls(row['name'], float(row['price']), int(row['quantity']))

        except FileNotFoundError:
            print("FileNotFoundError: Отсутствует файл item.csv")
            raise
        except InstantiateCSVError:
            print("InstantiateCSVError: Файл item.csv поврежден")
            raise



    @staticmethod
    def string_to_number(number: str):
        return int(float(number))