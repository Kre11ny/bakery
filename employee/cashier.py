from currency import Ruble
from employee import Employee
from menu import Menu


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

    def listen_client(self):
        self.greeting()
        print_client_action_options()
        option = read_client_option()
        # order = Order()

        while option != 0:
            if option == 1:
                self._menu.show()
                # здесь примерно нужно сделать заказ
                # order.add_postition(position_id)
            elif option == 2:
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
            elif option == 3:
                # здесь на объекте Order вызвать delete_position(postition_id) или что-то типа того также с валидацией внутри
            else:
                print_oops()

            print_client_action_options()
            option = read_client_option()

        # дальше тебе останется придумать, куда и как отдать заказ
        # а также как известить клиента, что заказ готов
        print('Всего доброго!')


def print_client_action_options():
    print('Что бы вы хотели сделать?')
    print('[0] Я передумал')
    print('[1] Сделать заказ')
    print('[2] Изменить позицию в заказе')
    print('[3] Удалить позицию в заказе')


def read_client_option() -> int:
    try:
        return int(input('Что бы вы хотели сделать?'))
    except ValueError:
        print_oops()


def print_oops():
    print("Упс... неверная опция. Попробуйте ещё раз 🙂")