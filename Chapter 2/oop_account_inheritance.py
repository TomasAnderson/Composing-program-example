class Account:
	"""A bank account that has a non-negative balance."""
	interest = 0.02
	def __init__(self, account_holder):
		self.balance = 0
		self.holder = account_holder
	def deposit(self, amount):
		"""Increase the account balance by amount and return the new balance."""
		self.balance = self.balance + amount
		return self.balance
	def withdraw(self, amount):
		"""Decrease the account balance by amount and return the new balance."""
		if amount > self.balance:
			return 'Insufficient funds'
		self.balance = self.balance - amount
		return self.balance

class CheckingAccount(Account):
	"""A bank account that charges for withdrawals."""
	withdraw_charges = 1
	interest = 0.01
	def withdraw(self, amount):
		return Account.withdraw(self, amount + self.withdraw_charges)

checking = CheckingAccount('Sam')
print(checking.deposit(10))
print(checking.withdraw(5))
print(checking.interest)