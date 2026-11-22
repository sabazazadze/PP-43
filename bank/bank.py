# სავარჯიშო 2: მოცემული კოდი (არ შეცვალოთ)
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("თანხა დადებითი უნდა იყოს")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("თანხა დადებითი უნდა იყოს")
        if amount > self.balance:
            raise ValueError("ანგარიშზე არასაკმარისი თანხაა")
        self.balance -= amount