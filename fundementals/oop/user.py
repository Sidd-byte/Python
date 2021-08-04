class User:

    def __init__(self, name):
        self.name = name
        self.amount = 0

    def make_deposit(self, amount):
        self.amount += amount

    def make_withdrawl(self, amount):
        self.amount -= amount

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.amount}")

damon = User("Damon")
pablo = User("Pablo")
sasha = User("Sasha")

damon.make_deposit(25)
damon.make_deposit(100)
damon.make_deposit(35)
damon.make_withdrawl(5)
damon.display_user_balance()

pablo.make_deposit(825)
pablo.make_deposit(375)
pablo.make_withdrawl(100)
pablo.make_withdrawl(175)
pablo.display_user_balance()

sasha.make_withdrawl(400)
sasha.make_withdrawl(700)
sasha.make_withdrawl(300)
sasha.display_user_balance()

msg = "hello world"
print(msg)