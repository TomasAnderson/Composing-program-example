def sum_naturals(n):
	total, k = 0, 1
	while k <= n:
		total, k = total + k, k + 1
	return total

# result = sum_naturals(100)
# print(result)

def sum_cubes(n):
	total, k = 0, 1
	while k <= n:
		total, k = total + k*k*k, k + 1
	return total

def pi_sum(n):
	total, k = 0, 1
	while k <= n:
		total, k = total + 8/((4*k-3) * (4*k-1)), k+1
	return total

def summation(n, term):
	total, k = 0, 1
	while k <= n:
		total, k = total + term(k), k + 1
	return total

def cube(x):
	return x * x * x

print(summation(100, cube), sum_cubes(100))


# result = pi_sum(10000)
# print(result)