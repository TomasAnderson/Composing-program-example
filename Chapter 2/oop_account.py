class Account:
	interest = 0.02
	def __init__(self, account_holder):
		self.balance = 0
		self.holder = account_holder
	def deposit(self, amount):
		self.balance = self.balance + amount
		return self.balance
	def withdraw(self, amount):
		if amount > self.balance:
			return 'Insufficient funds'
		self.balance -= amount
		return self.balance


a = Account('Kirk')
a.balance
a.holder

b = Account('Spock')
b.balance = 200
a is a
a is not b

c = a 
c is a
		
spock_account = Account('Spock')
spock_account.deposit(100)
spock_account.withdraw(90)
spock_account.withdraw(90)
spock_account.holder

getattr(spock_account, 'balance')
hasattr(spock_account, 'deposit')

type(Account.deposit) # <ckass 'function'>
type(spock_account.deposit) # <class 'method'>
"""self will be bound to the object automatically when method is called"""

kirk_account = Account('Kirk')
kirk_account.interest = 0.08
kirk_account.interest
spock_account.interest

Account.interest = 0.05
kirk_account.interest
spock_account.interest

