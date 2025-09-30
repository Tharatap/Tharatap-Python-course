class BankAccount:
    
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.__balance = initial_balance  # Private attribute
        self.__transaction_history = []   # Private attribute
    
    # Public method to access private balance
    def get_balance(self):
        return self.__balance
    
    # Public method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.__transaction_history.append(f"Deposit: +${amount}")
            return True
        return False
    
    # Public method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self.__transaction_history.append(f"Withdrawal: -${amount}")
            return True
        return False
    
    # Property decorator for read-only access
    
    @property # เอาไว้ดูค่าอย่างเดียว
    def transaction_history(self):
        return self.__transaction_history.copy()
    
    def __str__(self): # ย่อมาจาก string ทำให้เรา print วัตถุจาก class ได้ print ผ่านชื่อวัตถุของ class ได้เลย
        return f"Account {self.account_number}: Balance ${self.__balance}"

# Usage example
account = BankAccount("12345", 1000)
print(account.get_balance())  # 1000
account.deposit(500)
account.withdraw(200)
print(account)  # Account 12345: Balance $1300     (มันคือการ เรียกใช้ def __str__ แต่เราเรียกผ่านชื่อวัตถุได้เลย)
#print(account.transaction_history) เรียก transaction_history มาดูต้องเรียกผ่าน method เพราะเรา set ตัวแปร transaction_history ไว้เป็น private