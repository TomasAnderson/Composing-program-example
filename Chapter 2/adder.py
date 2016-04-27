def make_adder(n):
	def adder(k):
		return n + k
	return adder

add_three = make_adder(3)
print(add_three(4))