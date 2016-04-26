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
		if amount > self.balance:
			return "Insufficient funds"
		self.balance = self.balance - amount
		return self.balance

class CheckingAccount(Account):
	"""A bank account this charges for withdrawals"""
	withdraw_charge = 1
	interest = 0.01
	def withdraw(self, amount):
		return Account.withdraw(self, amount + self.withdraw_charge)


class SavingsAccount(Account):
	deposit_charge = 2
	def deposit(self, amount):
		return Account.deposit(self, amount - self.deposit_charge)

class AsSeenOnTVAccount(CheckingAccount, SavingsAccount):
	def __init__(self, account_holder):
		self.holder = account_holder
		self.balance = 1

such_a_deal = AsSeenOnTVAccount("John")
print(such_a_deal.deposit(20))
print(such_a_deal.withdraw(5))

"""Python supports multiple inheritence, and Python resolves
	 names from left to right, then upwards."""