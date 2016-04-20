def divisors(n):
	return [x for x in range(1,n) if n % x == 0]

perfect_number = [n for n in range(1, 1000) if sum(divisors(n)) == n]
print(perfect_number)