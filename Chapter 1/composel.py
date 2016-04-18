def composel(f, g):
	def h(x):
		return f(g(x))
	return h

def square(x):
	return x * x

def successor(x):
	return x + 1

square_successor = composel(square, successor)
result = square_successor(12)
print(result)