def normal_composal(f, g):
	def h(x):
		return f(g(x))
	return h

def lambda_composal(f, g):
	return lamda x: f(g(x))


