class Employees:

    def __init__(self, empID, empName, empPost, empSalary):
        self.empID = empID
        self.empName = empName
        self.empPost = empPost
        self.empSalary = empSalary

    def setEmpID(self, empID):
        self.empID = empID

    def getEmpID(self) -> int:
        return self.empID

    def setEmpName(self, empName):
        self.empName = empName

    def getEmpName(self) -> str:
        return self.empName

    def setEmpPost(self, empPost):
        self.empPost = empPost

    def getEmpPost(self) -> str:
        return self.empPost

    def setEmpSalary(self, empSalary):
        self.empSalary = empSalary

    def getEmpSalary(self) -> int:
        return self.empSalary

    def display_info(self):
        return f"{self.empID} Employee Name: {self.empName}, Position: {self.empPost}, Salary: {self.empSalary}"


employee_list = [
    [1, 'Alice', 'Cashier', 100000],
    [2, 'Bob', 'Baker', 100000],
    [3, 'Charlie', 'Manager', 150000]
]


# employees = [Employees(*data) for data in employee_list]

# for emp in employees:
# print(emp.display_info())


class Menu:
    add_products = []

    def __init__(self):
        self.baked_foods = {
            'Круассан': 50,
            'Булочка с корицей': 60,
            'Торт': 300,
            'Пирожное': 80,
            'Хлеб': 40
        }
        self.drinks = {
            'Кофе': 70,
            'Чай': 50,
            'Сок': 60,
            'Вода': 30
        }

    def display_menu(self):
        print("Меню выпечки:")
        for item, price in self.baked_foods.items():
            print(f"{item}: {price} руб.")

        print("\nМеню напитков:")
        for item, price in self.drinks.items():
            print(f"{item}: {price} руб.")

    def order(self):
        total = 0

        while True:
            choice = input('\nEnter the product name for the order/to complete the order, write "exit"):').capitalize()
            if choice.lower() == 'exit':
                break

            if choice in self.baked_foods:
                quantity = int(input(f"Введите количество: "))
                total += self.baked_foods[choice] * quantity
                self.add_products.append((choice, quantity))
                print(f'You have added to the order: {choice} in the following quantity: {quantity}')
            elif choice in self.drinks:
                quantity = int(input(f"Введите количество: "))
                total += self.drinks[choice] * quantity
                self.add_products.append((choice, quantity))
                print(f'You have added to the order: {choice}. In the following quantity: {quantity}')
            else:
                print('This product is not on the menu')

        print(f'\nThe total amount of your order: {total} руб.')
        print(f'Your order list: {self.add_products}')

    def deleted_products(self):
        for product in self.add_products:
            if product[0] in self.baked_foods or self.drinks:
                product_name = input(f'Введите название продукта,который желаете удалить: ').capitalize()
                quantity = int(input(f"Введите количество, которое хотите удалить: "))
                if product[1] > quantity:
                    product[1] -= quantity
                    print(f"Успешно удалено {quantity} шт. {product_name}.")
                elif product[1] == quantity:
                    del self.add_products[product]
                    print(f"Продукт {product_name} полностью удален из корзины.")
                else:
                    print(f"В корзине недостаточно шт для удаления.")

            else:
                print(f"Продукт {product_name} не найден в корзине.")
            Menu().deleted_products()


# Menu().display_menu()
# Menu().order()
# Menu().deleted_products()
