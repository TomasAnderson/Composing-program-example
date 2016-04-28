def make_adder(n):
	def adder(k):
		return n + k
	return adder

# add_three = make_adder(3)
# print(add_three(4))

class Adder(object):
	def __init__(self, n):
		self.n = n
	def __call__(self, k):
		return self.n + k

# add_three_obj = Adder(3)
# print(add_three_obj(4))