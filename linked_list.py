'''
Basic implementation of a singly linked list

We want the list to support these operations:

- get: return the element at a specific index
- set: modify the element at a specific index
- add: insert a new element at a specific index
- delete: remove the element at a specific index (to be completed in HW 3)
'''

# This class represents a single node of the linked list
# Each node contains its data, and a reference to the next node in the list
class Node:
	# Constructor
	def __init__(self, data, next_node):
		self.data = data
		self.next_node = next_node


# This class represents a linked list - a collection of Node objects.  The list
# keeps track of the head node.  From there, we can get to any other node in
# the list by following the next_node references.
class LinkedList:
	# Constructor
	def __init__(self):
		# In an empty list, the head reference points to None
		self.head = None

		# This attribute keeps track of how many nodes are in the list
		# (handy for validating indices in some of the later methods)
		self.size = 0

	# The __str__ method traverses the list to see what data is inside
	def __str__(self):
		result = 'head -> '

		# List traversal - we set up a new reference (temp) to the head, and
		# repeatedly move temp down the list until it points to None
		temp = self.head
		while temp != None:
			# Get temp's data
			result += str(temp.data) + ' -> '

			# Move temp to the next node in the list
			temp = temp.next_node

		result += 'None'
		return result





	# Returns the element at a specific index (must be non-negative), or raises
	# an error if an invalid index is provided
	def get(self, index):
		# Make sure index is valid
		if 0 <= index < self.size:
			# Move temp down the list index times
			temp = self.head
			for i in range(index):
				temp = temp.next_node

			# Return temp's data
			return temp.data
		else:
			raise IndexError(f'Invalid index provided: {index}, valid values are {0}-{self.size - 1}')


	# Changes the element at a specific index (must be non-negative), or raises
	# an error if an invalid index is provided
	def set(self, index, new_data):
		# Almost exactly the same code as get, except we *change* temp's data
		# rather than returning it after the traversal loop
		if 0 <= index < self.size:
			temp = self.head
			for i in range(index):
				temp = temp.next_node
			temp.data = new_data
		else:
			raise IndexError(f'Invalid index provided: {index}, valid values are {0}-{self.size - 1}')



	# Adds a new node to the head (front) of the list
	def add_to_head(self, new_data):
		self.head = Node(new_data, self.head)
		self.size += 1

	# Adds a new node to any index of the list (index must be non-negative),
	# or raises an error if an invalid index is provided
	def add(self, index, new_data):
		# Index 0 is the head, so just call the existing add_to_head method
		if index == 0:
			self.add_to_head(new_data)

		# Check index to be sure it's valid
		# Note that self.size *is* a valid index here -- that means adding to
		#  the very end of the list
		elif 0 < index <= self.size:
			# Get to the node at (index - 1)
			temp = self.head
			for i in range(index - 1):
				temp = temp.next_node
			# Insert the new node after (index - 1)
			temp.next_node = Node(new_data, temp.next_node)
			self.size += 1
		else:
			raise IndexError(f'Invalid index provided: {index}, valid values are {0}-{self.size}')


	# Removes the first (head) node from the list, or raises an error if the
	# list is empty
	def delete_from_head(self):
		if self.size > 0:
			self.head = self.head.next_node
			self.size -= 1
		else:
			raise ID10TError()


	# def delete(self, index):
	# 	if index == 0:
	# 		delete_from_head()
	# 	elif 0 < index < self.size:
	# 		temp = self.head
	# 		for i in range(index - 1):
	# 			temp = temp.next_node

	# 		new_temp = self.head
	# 		for j in range(index):
	# 			new_temp = new_temp.next_node
	# 		temp.next_node = new_temp.next_node
	# 		self.size -= 1
	# 	else:
	# 		raise IndexError()




	def delete(self, index):
		if index == 0:
			self.delete_from_head()
		elif 0 < index < self.size:
			temp = self.head
			for i in range(index - 1):
				temp = temp.next_node

			new_temp = self.head
			for j in range(index):
				new_temp = new_temp.next_node
			temp.next_node = new_temp.next_node
			self.size -= 1
		else:
			raise IndexError()

	def delete_target(self, target):
		temp = self.head
		while temp.data != None:
			if temp.data != target:
				temp = temp.next_node

			elif temp.data == target:
				new_temp = temp
				temp = temp.next_node
				new_temp = new_temp.next_node
				self.size -= 1
				return temp.data

		return None


	def __eq__(self, other):
		if not isInstance(other, LinkedList):
			return False
			if self.size != other.size:
				return False
			temp, new_temp = self.head, other.head
			for i in range(self.size):
				if temp.data != new_temp.data:
					return False
				temp, new_temp = temp.next_node, new_temp.next_node

		return True





















# Example of a custom exception type -- simply create a subclass of Exception
class ID10TError(Exception):
	# No need to do anything else
	pass


# Test code
stuff = LinkedList()
print(stuff)

print('\nTesting add_to_head...')
for d in [7, 5, 20]:
	stuff.add_to_head(d)
	print(stuff)

print('\nTesting get...')
for i in range(3):
	print(stuff.get(i))
# stuff.get(3)

print('\nTesting set...')
stuff.set(1, 'sloth')
print(stuff)

print('\nTesting add...')
stuff.add(0, 'test')
print(stuff)
stuff.add(2, 'new index 2')
print(stuff)
stuff.add(5, 'new last element')
print(stuff)

# print('\nTesting delete_from_head...')
# for i in range(7):
# 	stuff.delete_from_head()
# 	print(stuff)


	# def delete(self, index):
	# 	if index == 0:
	# 		delete_from_head()
	# 	elif 0 < index < self.size:
	# 		temp = self.head
	# 		for i in range(index - 1):
	# 			temp = temp.next_node

	# 		new_temp = self.head
	# 		for j in range(index):
	# 			new_temp = new_temp.next_node
	# 		temp.next_node = new_temp.next_node
	# 		self.size -= 1
	# 	else:
	# 		raise IndexError()

	# def delete_target(self, target):
	# 	temp = self.head
	# 	while temp.data != None:
	# 		if temp.data != target:
	# 			temp = temp.next_node

	# 		elif temp.data == target:
	# 			new_temp = temp
	# 			temp = temp.next_node
	# 			new_temp = new_temp.next_node
	# 			self.size -= 1
	# 			return temp.data

	# 	return None


	# def __eq__(self, other):
	# 	if not isInstance(other, LinkedList):
	# 		return False
	# 		if self.size != other.size:
	# 			return False
	# 		temp, new_temp = self.head, other.head
	# 		for i in range(self.size):
	# 			if temp.data != new_temp.data:
	# 				return False
	# 			temp, new_temp = temp.next_node, new_temp.next_node

	# 	return True


test_list = LinkedList()

for i in range(10):
	test_list.add_to_head(i)
print(test_list)

# delete from the head of a list with several nodes
test_list.delete(0)
print(test_list)

# delete from the middle of a list with several nodes
test_list.delete(5)
print(test_list)

# delete from the tail of a list with several nodes
test_list.delete(test_list.size - 1)
print(test_list)


targeted_test_list = LinkedList()

for i in range(10):
	targeted_test_list.add_to_head(i)
targeted_test_list.add_to_head('head')

# delete target from head of a list with several nodes
print(targeted_test_list)
targeted_test_list.delete_target('head')
print(targeted_test_list)

# delete target from middle of a list with several nodes
targeted_test_list.delete_target('4')
print(targeted_test_list)

# delete target from tail of a list with several nodes
targeted_test_list.delete_target('9')
print(targeted_test_list)

# delete target from a non-empty list that doesn't contain the target
targeted_test_list.delete_target('sloth')
print(targeted_test_list)

# delete target from an empty list
empty_list = LinkedList()
print(empty_list)
empty_list.delete_target('empty')


# test equality of two non-empty lists that are equal
new_list = LinkedList()
for x in [1, 'sloth', 'bear', 'pig']:
	new_list.add_to_head(d)
print(new_list)
newer_list = new_list
print(newer_list)

print(new_list == newer_list)


# test equality of two lists that contain the same elements up
# to a certain point, but one list keeps going
new_list.add(4, 'more')
new_list.add(5, 'elements')
print(new_list)
print(newer_list)
print(new_list == newer_list)


# test equality between two list with same number of elements, 
# but elements do not match

x = LinkedList()
y = LinkedList()
for h in [1, 2, 3]:
	x.add_to_head(h)
for j in [a, b, c]:
	y.add_to_head(j)

print(x == y)


# test equality between non-empty list and empty list
print(x == empty_list)

# test equality between two empty lists

also_empty_list = LinkedList()
print(empty_list == also_empty_list)

# test equality between non-empty list and non-LinkedList object
z = [1, 2, 3]
print(x)
print(z)
print(x == z)