
def flatten_help(arg, re):
	for element in arg:
		if type(element) is list:
			flatten_help(element, re)
		elif element is not None:
			re.append(element)
	return re

def flatten(arg):
	re = []
	flatten_help(arg, re)
	return re

print flatten([0, 2, [[2, 3], 8, 100, None, [[None]]], -2])
# [0, 2, 2, 3, 8, 100, -2]

print flatten([0, "2", [[2, "hello![][][]"], 8, {"A":1,"b":2}, None, [[None]]], -2])
# [0, '2', 2, 'hello![][][]', 8, {'A': 1, 'b': 2}, -2]

print flatten([[],[],[],[],[],[[[[[[]]]]]],[]])
# []
