def make_withdraw(balance):
	"""Return a withdraw function that draws down balance with each call"""
	def withdraw(amount):
		nonlocal balance # Declare the name "balance" nonlocal
		if amount > balance:
			return "Insufficient funds"
		balance = balance - amount
		return balance
	return withdraw

# wd = make_withdraw(20)
# print(wd(5))
# print(wd(3))

wd = make_withdraw(20)
wd2 = make_withdraw(7)
print(wd2(6))
print(wd(8))