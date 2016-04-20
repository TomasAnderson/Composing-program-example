def make_withdraw(balance):
	"""Return a withdraw function that draws down balance with each call"""
	def withdraw(amount):
		nonlocal balance # Declare the name "balance" nonlocal
		if amount > balance:
			return "Insufficient funds"
		balance = balance - amount
		return balance
	return withdraw