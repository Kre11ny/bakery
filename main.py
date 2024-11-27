from bakery.main_Bakery import Menu
import time


def loading():
    print('Инициализация системы\nЗагрузка пекарни\n')
    time.sleep(0.3)
    char = '|'
    for i in range(101):
        time.sleep(0.1)
        print('\rЗагрузка:', i * char, str(i), '%', end='')
    time.sleep(0.5)
    print('\nСистема успешно загружена')
    time.sleep(0.3)
    print('Добро пожаловать в пекарню')
    time.sleep(0.3)


def main():
    loading()


if __name__ == '__main__':
    main()


# print(Menu().display_menu())

def menu():
    print('[1] Make an order')
    print('[2] Delete an order')
    print('[0] Exit the program')


menu()
option = int(input('Enter your option: '))

while option != 0:
    if option == 1:
        Menu().display_menu()
        Menu().order()
    elif option == 2:
        Menu().deleted_products()
    else:
        print('Invalid option')
    print()
    menu()
    option = int(input('Enter your option: '))
print('Thanks for using this program. Goodbye.')
