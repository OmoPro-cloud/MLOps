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
  def __init__(self, account_number, account_holder, balance):
    self.__account_number = account_number
    self.__account_holder = account_holder
    self.__balance = balance

  def get_details(self):
    return f'{self.__account_holder} currently has active account: "{self.__account_number}" on file with us. {self.__account_holder} has a remaining balance of ${self.__balance}.'
  
  def withdraw(self, amount):
    if amount <= 0:
      print('Sorry, your withdrawal amount must be greater than 0!')
    self.__balance -= amount
    return f'Congratulations, {self.__account_holder}! You have succesfully made a withdrawal amount of: ${amount}. Your current balance is now: {self.__balance}.'
  
  def deposit(self, amount):
    if amount <= 0:
      print('Sorry, your selected deposit amount has to be greater than $0!')
    self.__balance += amount
    return f'Congratulations, {self.__account_holder}! Your deposit amount of ${amount} has been processed, and your account has dually been updated to reflect its new balance of {self.__balance}!'


myAccount = bankAccount(619, 'Jay', 7000000)

print(myAccount.get_details())
print(myAccount.withdraw(30000))
print(myAccount.deposit(150000))