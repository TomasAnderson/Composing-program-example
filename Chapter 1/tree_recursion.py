def fib(n):
	if n == 1:
		return 0
	if n == 2:
		return 1
	else:
		return fib(n-2) + fib(n-1)

# print(fib(6))

def count_partitions(n, m):
	"""Count the ways to partition n using parts up to m. """
	if n == 0:
		return 1
	elif n < 0:
		return 0
	elif m == 0:
		return 0
	else:
		return count_partitions(n-m, m) + count_partitions(n, m-1)

print(count_partitions(5,5))
print(count_partitions(10,10))
print(count_partitions(15,15))
