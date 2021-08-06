


class BankAccount:
    
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
        print(f"Balance: {self.balance}")
        return self
    
    def yeild_intrest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self 

savings = BankAccount(.03, 1000)
checkings = BankAccount(.02, 5000)


savings.deposit(10).deposit(100).deposit(50).withdrawl(40).yeild_intrest().display_balance()
checkings.deposit(12).deposit(111).withdrawl(25).withdrawl(7).yeild_intrest().display_balance()






