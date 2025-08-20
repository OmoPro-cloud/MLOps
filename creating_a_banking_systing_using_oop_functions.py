#Assignment – Banking System (Encapsulation & Inheritance)
#Objective: Practice Encapsulation and Inheritance by modeling a small banking system.

#Instructions:

#Create a BankAccount class with:

#Private attributes: account number, account holder name, and balance.

#Getter methods to view account details.

#Methods to deposit and withdraw money (with validation).

#Create a SavingsAccount class that inherits from BankAccount:

#Add an attribute for interest rate.
#Add a method to calculate and apply interest.

#Create a CurrentAccount class that inherits from BankAccount:

#Add an overdraft limit.

#Modify withdrawal logic to allow overdraft within the limit.

#Write a main program to:

#Create one savings account and one current account.

#Perform deposits, withdrawals, and interest calculations.

#Print updated account details.

#Expected Skills Practiced:

#Private attributes & methods (Encapsulation)

#Class inheritance

#Method overriding


# 1. BankAccount
class BankAccount:
    def __init__(self, account_number, holder_name, balance=0):
        self.__account_number = account_number
        self.__holder_name = holder_name
        self.__balance = balance

    def get_account_number(self):
        return self.__account_number

    def get_holder_name(self):
        return self.__holder_name

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f'Deposited: {amount}')
        else:
            print('Deposit amount must be positive.')

    def withdraw(self, amount):
        if amount <= 0:
            print('Withdrawal amount must be positive.')
        elif amount > self.__balance:
            print('Insufficient funds.')
        else:
            self.__balance -= amount
            print(f'Withdrew: {amount}')

    def print_account_details(self):
        print(f'Account Number: {self.get_account_number()}')
        print(f'Account Holder: {self.get_holder_name()}')
        print(f'Balance: {self.get_balance()}')
        print('-' * 30)


# 2. SavingsAccount class
class SavingsAccount(BankAccount):
    def __init__(self, account_number, holder_name, balance, interest_rate):
        super().__init__(account_number, holder_name, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.get_balance() * (self.interest_rate / 100)
        self.deposit(interest)
        print(f'Interest of {interest} applied at rate {self.interest_rate}%.')


# 3. CurrentAccount class
class CurrentAccount(BankAccount):
    def __init__(self, account_number, holder_name, balance, overdraft_limit):
        super().__init__(account_number, holder_name, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= 0:
            print('Withdrawal amount must be positive.')
        elif amount > self.get_balance() + self.overdraft_limit:
            print('Overdraft limit exceeded.')
        else:
            new_balance = self.get_balance() - amount
            self._BankAccount__balance = new_balance
            print(f'Withdrew: {amount}')


# 4. Main program
def main():
    savings = SavingsAccount('619', 'Jay', 70000, 5)
    print('Savings Account')
    savings.print_account_details()
    savings.deposit(500)
    savings.withdraw(200)
    savings.apply_interest()
    savings.print_account_details()

    current = CurrentAccount('C456', 'Bob', 180, 300)
    print('Current Account:')
    current.print_account_details()
    current.deposit(200)
    current.withdraw(800)
    current.withdraw(100) 
    current.print_account_details()

# Run the main program
if __name__ == '__main__':
    main()