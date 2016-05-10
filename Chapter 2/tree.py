def tree(root, branches=[]):
	for branch in branches:
		assert is_tree(branch), 'branch must be tree'
	return [root] + list(branches)

def root(tree):
	return tree[0]

def branches(tree):
	return tree[1:]

def is_tree(tree):
	if type(tree) != list or len(tree) < 1:
		return False
	for branch in branches(tree):
		if not is_tree(branch):
			return False
	return True

def is_leaf(tree):
	return not branches(tree)

def fib_tree(n):
	if n == 0 or n == 1:
		return tree(n)
	else:
		left, right = fib_tree(n-2), fib_tree(n-1)
		fib_n = root(left) + root(right)
		return tree(fib_n, [left, right])

# print(fib_tree(5))

def count_leaves(tree):
	if is_leaf(tree):
		return 1
	else:
		branch_count = [count_leaves(b) for b in branches(tree)]
		return sum(branch_count)

# print(count_leaves(fib_tree(5)))


def partition_tree(n, m):
	if n == 0:
		return tree(True)
	elif n < 0 or m == 0:
		return tree(False)
	else:
		left = partition_tree(n-m, m)
		right = partition_tree(n, m-1)
		return tree(m, [left, right])


# print(partition_tree(2, 2))

def print_parts(tree, partition=[]):
	if is_leaf(tree):
		if root(tree):
			print(' + '.join(partition))
	else:
		left, right=branches(tree)
		m = str(root(tree))
		print_parts(left, partition + [m])
		print_parts(right, partition)

# print_parts(partition_tree(6, 4))

print(partition_tree(6, 4))