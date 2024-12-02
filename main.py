from bakery import Bakery
from menu import Menu
import time
from collections import deque
import random
import asyncio
from storage import Storage


class RunSome:
    def __init__(self, task_count=5):
        self.task_count = task_count
        self.running = set()
        self.waiting = deque()

    @property
    def running_task_count(self):
        return len(self.running)

    def add_task(self, coro):
        if len(self.running) >= self.task_count:
            self.waiting.append(coro)
        else:
            self._start_task(coro)

    def _start_task(self, coro):
        # Add task to the set. This creates a strong reference to avoid mid-execution GC.
        self.running.add(coro)
        asyncio.create_task(self._task(coro))

    async def _task(self, coro):
        try:
            return await coro
        finally:
            self.running.remove(coro)
            if self.waiting:
                self._start_task(self.waiting.popleft())


async def main():
    runner = RunSome()

    async def rand_delay():
        rnd = random.random() + 0.5
        print("Task started", asyncio.current_task().get_name(),
              runner.running_task_count)
        await asyncio.sleep(rnd)
        print("Task ended", asyncio.current_task().get_name(),
              runner.running_task_count)

    for _ in range(10):
        runner.add_task(loading())
    # keep the program alive until all the tasks are done
    while runner.running_task_count > 0:
        await asyncio.sleep(0.1)


async def loading():
    print(f"started at {time.strftime('%A %X')}")
    print('Инициализация системы')
    print('Загрузка пекарни')
    time.sleep(0.2)
    char = '|'
    for i in range(101):
        time.sleep(0.01)
        print('\rЗагрузка:', i * char, str(i), '%', end='')
    print()
    time.sleep(0.5)
    print('Система успешно загружена')
    time.sleep(0.2)
    print('Добро пожаловать в пекарню')
    print(f"ended at {time.strftime('%X')}")


if __name__ == '__main__':
    stor = Storage()
    menu = Menu(
        stor.get_baked_foods(),
        stor.get_drinks(),
    )
    cashier = stor.get_cahier()
    cashier.take_menu(menu)

    rogalik = Bakery(
        cashier,
        stor.get_baker(),
        stor.get_manager(),
    )
    rogalik.print_personal()
    rogalik.serve()
    # some_new_person = Person("John Smith")
    # loading()
    # listen_client()
    # asyncio.run(main())

# print(Menu().display_menu())
