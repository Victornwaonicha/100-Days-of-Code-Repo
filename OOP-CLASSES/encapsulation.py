#### ENCAPSULATION ####

class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number # Encapsulated attribute.
        self._balance = balance # Encapsulated attribute.
        
    def deposit(self, amount):
        self._balance += amount
        
    def withdraw(self, amount):
        if amount <= self._balance:
             self._balance -= amount
        else:
            print("Insufficient Funds")
        
    def get_balance(self):
        return self._balance
    
# Creating an instance of BankAccount class.
account1 = BankAccount("123456789", 10000)

# Accessing methods to interact with the encapsulated attributes.
account1.deposit(500)
account1.withdraw(200)

print("Your current balance:", account1.get_balance())
        
        
    