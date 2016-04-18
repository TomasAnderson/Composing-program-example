def sum_digits(x):
	if x < 0:
		return sum_digits(abs(x))
	elif x < 10:
		return x
	else:
		all_but_last, last = x // 10, x % 10
		return sum_digits(all_but_last) + last

# print(sum_digits(-123456789))

def fact_iter(n):
	total, k = 1, 1
	while k <= n:
		total, k = total * k, k + 1
	return total

print(fact_iter(4))

def fact(n):
	if n == 1:
		return 1
	else:
		return n * fact(n - 1)

print(fact(4))