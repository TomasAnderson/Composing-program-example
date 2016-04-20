def right_binarize(tree):
	"""Construct a right-branching binary tree."""
	if is_leaf(tree):
		return tree
	if len(tree) > 2:
		tree = [tree[0], tree[1:]]
	return [right_binarize(b) for b in tree]

def is_leaf(tree):
	return type(tree) is int

binarized = right_binarize(range(1, 8))
print(binarized)