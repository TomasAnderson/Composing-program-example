def account(initial_balance):
	dispatch = {
		'deposit': deposit,
		'withdraw': withdraw,
		'balance': initial_balance
	}

	def deposit(amount):
		dispatch['balance'] += amount
		return dispatch['balance']
	def withdraw(amount):
		if amount > dispatch['balance']:
			return 'Insufficient funds'
		dispatch['balance'] -= amount
		return dispatch['balance']
	return dispatch

def withdraw(account, amount):
	return account['withdraw'](amount)

def deposit(account, amount):
	return account['deposit'](amount)

def check_balance(account):
	return account['balance']

a = account(20)
print(deposit(a, 5))
print(withdraw(a, 17))
print(check_balance(a))