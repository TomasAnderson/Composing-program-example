def cascade(n):
	if n < 10:
		print(n)
	else:
		print(n)
		cascade(n // 10)
		print(n)

# cascade(2013)

def cascade2(n):
	print(n)
	if n >= 10:
		cascade2(n//10)
		print(n)

# cascade2(2013)

def is_even(n):
	return n % 2 == 0

def play_alice(n):
	if n == 0:
		print("Bob wins!")
	else:
		play_bob(n-1)

def play_bob(n):
	if n == 0:
		print("Alice wins!")
	elif is_even(n):
		play_alice(n-2)
	else:
		play_alice(n-1)

play_alice(22)