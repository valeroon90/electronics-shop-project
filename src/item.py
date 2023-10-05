import csv
import os

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


    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity


    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * Item.pay_rate


    @property
    def name(self):
        return self.__name


    @name.setter
    def name(self, data_str: str):
        if len(data_str) > 10:
            self.__name = data_str[:10]
        self.__name = data_str


    @classmethod
    def instantiate_from_csv(cls):
        Item.all = []
        with open('..\src\items.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
               cls(row['name'], float(row['price']), int(row['quantity']))



    @staticmethod
    def string_to_number(number: str):
        return int(float(number))


