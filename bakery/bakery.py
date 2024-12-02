from employee import Cashier, Baker, Manager


class Bakery:
    def __init__(self, cashier: Cashier, baker: Baker, manager: Manager):
        self._cashier = cashier
        self._baker = baker
        self._manager = manager

    def print_personal(self):
        print(self._cashier)
        print(self._baker)
        print(self._manager)

    def serve(self):
        self._cashier.listen_client()
