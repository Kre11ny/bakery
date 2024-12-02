from client import Client
from currency import Ruble
from employee import Employee
from menu import Menu
from order import Order


class Cashier(Employee):
    def __init__(self, name: str, salary: Ruble):
        super().__init__(name, salary)
        self._position: str = 'Cashier'
        self._menu: Menu = None

    def set_position(self, position: str):
        self._position: str = position

    def get_position(self) -> str:
        return self._position

    def __str__(self):
        return f'{self.get_position()}: {self.get_name()}'

    def take_menu(self, menu: Menu):
        self._menu: Menu = menu

    def greeting(self):
        print(f'Здравствуйте! Меня зовут {self.get_name()}')

    def register_client(self) -> Client:
        self.greeting()
        input_name = input('Как Вас зовут?\n')  # TODO: возможно лишний перенос строки - протестировать!
        input_balance = safe_float_input_read(
            'Сколько у Вас денег\n')  # TODO: переделать потом на валидацию средств внутри клента
        print(f'Рады Вас приветствовать в нашей Пекарне, {input_name}!')

        return Client(input_name, input_balance)

    def accept_order_from_client(self, client: Client):
        option_question = 'Что бы вы хотели сделать?\n'
        print_client_action_options()
        option = safe_int_input_read(option_question)
        order = Order()

        while option != 0:
            if option == 1:
                self.offer_and_accept_backed(client, order)
                print('Желаете что-нибудь ещё из выпечки?')
                print('[0] Нет')
                print('[1] Да')
                decision = safe_int_input_read('Введите, пожалуйста, число: ')
                if decision == 1:
                    continue


            # elif option == 2:
            # здесь на объекте Order произвести требуемые изменения с правильными диалогами и ВАЛИДАЦИЕЙ ИЗМЕНЕНИЙ
            # внутри заказа должны быть все проверки на возможность удаления
            # можно бросить кастомный Exception и здесь его поймать, сказать при этом что-либо клиенту, например:
            # try:
            # order.remove_position(position_id, count)
            # except MyExceptionName:
            # print('oops...')
            # except MyExceptionName2:
            # print('oops2...')
            # в нашей первой домашке я создавал кастомный Exception, можно там глянуть, как это сделать
            # elif option == 3:
            # здесь на объекте Order вызвать delete_position(postition_id) или что-то типа того также с валидацией внутри
            else:
                print_oops()

            print_client_action_options()
            option = safe_int_input_read(option_question)

        print(f'{order}')
        # дальше тебе останется придумать, куда и как отдать заказ
        # а также как известить клиента, что заказ готов
        print('Всего доброго!')

    def offer_and_accept_backed(self, client: Client, order: Order):
        print(f'{client.get_name()}, выберите что-нибудь из выпечки 🙂')
        self._menu.show_backed()
        position_index = safe_int_input_read('Какую позицию хотели бы добавить в заказ? Укажите цифру: ')
        required_backed_position = self._menu.get_backed_by_index(position_index)
        order.add_position(
            required_backed_position.get_id(),
            required_backed_position.get_name(),
            required_backed_position.get_cost(),
            1,
        )
        print(f'Товар {required_backed_position} добавлен в заказ!')


def print_client_action_options():
    print('Что бы вы хотели сделать?')
    print('Введите, пожалуйста, цифру:')
    print('[0] Я передумал')
    print('[1] Сделать заказ')
    print('[2] Изменить позицию в заказе')
    print('[3] Удалить позицию в заказе')


def safe_int_input_read(text: str) -> int:
    try:
        return int(input(text))
    except ValueError:
        print_oops()


def safe_float_input_read(text: str) -> float:
    try:
        return float(input(text))
    except ValueError:
        print_oops()


def print_oops():
    print('Упс... неверная опция. Помните, нужно указать цифру опции! Попробуйте ещё раз 🙂')
