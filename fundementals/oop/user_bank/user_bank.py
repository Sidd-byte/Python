class BankAccount:
    account = []
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
    
    def withdrawl(self, amount):
        if(self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a 5 dollar fee")
            self.balance -= 5
        return self
    
    def deposit(self, amount):
        self.balance += amount
        return self

    def display_balance(self):
        return f"{self.balance}"
        return self
    
    def yeild_intrest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self 

class User:

    def __init__(self, name):
        self.name = name
        self.account = BankAccount(.05, 1000)

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account.display_balance()}")

    def transfer_money(self,amount,user):
        self.amount -= amount
        user.amount -= amount
        self.display_user_balance()
        user.display_user_balance()
        return self

damon = User("Damon")

damon.account.deposit(100)
damon.display_user_balance()