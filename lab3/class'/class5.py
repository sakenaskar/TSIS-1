class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self):
        print(self.balance)
    
    def withdraw(self):
        self.a = self.balance
        self.x = int(input())
        self.a = self.a - self.x
        if self.x <= self.balance:
            print ("Operation was successfully completed!")
            print ("Account balance: ",self.a)
            self.balance = self.a
        else:
            print("Not enough funds on deposit.")

str = str(input())
x = int(input())
a = Account(str,x)
a.deposit()
a.withdraw()