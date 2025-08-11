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

class bankAccount():
  def __init__(self, account_holder, account_number, account_balance):
    self.__account_holder = account_holder
    self.__account_number = account_number
    self.__account_balance = account_balance

    def get_balance():
      return f'Current balance = ${self.__account_balance}.'
    

  def get_details(self):
    return f'welcome, {self.__account_holder}. you currently hold account number #{self.__account_number}, with an available balance of ${self.__account_balance}'
  
  def deposit(self, amount):
    if amount <= 0:
      print('sorry {self.__acount_holder}, your deposit amount has to be greater than $0!')
    self.__account_balance += amount
    return f'congratulations {self.__account_holder}, your deposit of ${amount} has been succesfully processed, leaving you with an available balance of: ${self.__account_balance}'
  

  def withdraw(self, amount):
    if amount <= 0:
      print('sorry {self.__account_holder}, your withdrawal amount has to be greater than $0!')
    self.__account_balance -= amount
    return f'congratulations {self.__account_holder}, your withdrawal of ${amount} has been succesfully processed, leaving you with a remaining balance of: ${self.__account_balance}'

class savingsAccount(bankAccount):
  def __init__(self, account_number, account_holder, account_balance, interest_rate):
    bankAccount.__init__(self, account_number, account_holder, account_balance)
    self.__interest_rate = interest_rate

  def apply_interest(self):
    interest = self.__account_balance() * (self.__interest_rate / 100)
    response = self.deposit(interest)
    return (f'Interest of ${interest:.2f} added at {self.__interest_rate}%.' + (response))



myAccount = bankAccount('Jay', 619, 7000000)
print(myAccount.get_details())
print(myAccount.deposit(500000))
print(myAccount.withdraw(25000))

s = savingsAccount(123, 'Jay', 1000, 5)

print(s.get_details())
print(s.apply_interest())
print(s.get_details())