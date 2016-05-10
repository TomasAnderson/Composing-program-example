empty = 'empty'

def is_link(s):
	return s == empty or (len(s) == 2 and is_link(s[1]))

def link(first, rest):
	assert is_link(rest), 'rest must be a link'
	return [first, rest]

def first(list):
	assert is_link(list)
	assert list != empty
	return list[0]

def rest(list):
	assert is_link(list)
	assert list != empty
	return list[1]

four = link(1, link(2, link(3, link(4, empty))))
# print(first(four))
# print(rest(four))


def len_link_recursive(list):
	if list == empty:
		return 0
	elif rest(list) == empty:
		return 1
	else:
		return 1 + len_link_recursive(rest(list))

def len_link_iterative(list):
	length = 0
	while list != empty:
		list, length = rest(list), length + 1
	return length

def get_item_recursive(k, list):
	assert k >= 0
	assert list != empty
	if k == 0:
		return first(list)
	else:
		return get_item_recursive(k-1, rest(list))

def get_item_iterative(k, list):
	while k > 0:
		assert k > 0
		assert list != empty
		list, k = rest(list), k-1
	return first(list) 		

# print(len_link_recursive(four))
# print(len_link_iterative(four))
# print(get_item_recursive(1, four))
# print(get_item_iterative(1, four))

def extend_list(list1, list2):
	if list1 == empty:
		return list2
	else:
		return link(first(list1), extend_list(rest(list1), list2))

# print(extend_list(four, four))

def apply_to_all_link(list, fn):
	if list == empty:
		return list
	else:
		return link(fn(first(list)), apply_to_all_link(rest(list), fn))

# print(apply_to_all_link(four, lambda x: x*x))

def keep_if_link(list, filter):
	if list == empty:
		return list
	elif filter(first(list)):
		return link(first(list), keep_if_link(rest(list), filter))
	else:
		return keep_if_link(rest(list), filter)

# print(keep_if_link(four, lambda x: x%2==0))

def join_link(list, separator):
	if list == empty:
		return ""
	elif rest(list) == empty:
		return str(first(list))
	else:
		return str(first(list)) + separator + join_link(rest(list), separator)

# print(join_link(four, ', '))

def partitions(n, m):
	if n == 0:
		return link(empty, empty)
	elif n < 0 or m == 0:
		return empty
	else:
		using_m = partitions(n-m, m)
		with_m = apply_to_all_link(using_m, lambda s: link(m, s))
		without_m = partitions(n, m-1)
		return extend_list(with_m, without_m)

def print_partitions(n, m):
	lists = partitions(n, m)
	strings = apply_to_all_link(lists, lambda s: join_link(s, ' + '))
	print(join_link(strings, "\n"))

print_partitions(6, 4)
 

