from backed import Backed
from drink import Drink
from product import Product


class Menu:
    add_products = []
    total = 0

    def __init__(self, baked: [Backed], drinks: [Drink]):
        self._baked_foods: [Backed] = baked
        self._drinks: [Drink] = drinks

    def show_backed(self):
        print('Выпечка:')
        for i, item in enumerate(self._baked_foods):
            print(f'[{i}] {item}: {item.get_cost()}')

    def show_drinks(self):
        print('Напитки:')
        for i, item in enumerate(self._drinks):
            print(f'[{i}] {item}: {item.get_cost()}')

    def get_backed_by_index(self, i: int) -> Backed:
        try:
            return self._baked_foods[i]
        except KeyError:
            print('Такой выпечки в меню нет')

    def get_drink_by_index(self, i: int):
        try:
            return self._drinks[i]
        except KeyError:
            print('Такого напитка в меню нет')

    def order(self):
        while True:
            choice = input('\nEnter the product name for the order/to complete the order, write "exit"):').capitalize()
            if choice.lower() == 'exit':
                break

            if choice in self._baked_foods:
                quantity = int(input(f"Введите количество: "))
                self.total += self._baked_foods[choice] * quantity
                self.add_products.append([choice, quantity])
                print(f'You have added to the order: {choice} in the following quantity: {quantity}')
            elif choice in self._drinks:
                quantity = int(input(f"Введите количество: "))
                self.total += self._drinks[choice] * quantity
                self.add_products.append([choice, quantity])
                print(f'You have added to the order: {choice}. In the following quantity: {quantity}')
            else:
                print('This product is not on the menu')

        print(f'\nThe total amount of your order: {self.total} руб.')
        print(f'Your order list: {self.add_products}')

    def deleted_products(self):
        user_input_product_name = input(f'Введите название продукта,который желаете удалить: ').capitalize()
        product_exists = False

        for product in self.add_products:
            product_name = product[0]
            if user_input_product_name != product_name:
                continue

            product_exists = True

            quantity = int(input(f"Введите количество, которое хотите удалить: "))
            if product[1] > quantity:
                product[1] -= quantity
                print(f"Успешно удалено {quantity} шт. {user_input_product_name}.")
            elif product[1] == quantity:
                del self.add_products[product]
                print(f"Продукт {user_input_product_name} полностью удален из корзины.")
            else:
                print(f"В корзине недостаточно шт для удаления.")
        print(f"New basket: {self.add_products}. New total of order: {self.total}")
        # Menu().deleted_products()

        if not product_exists:
            print(f"Продукт {user_input_product_name} не найден в корзине.")
