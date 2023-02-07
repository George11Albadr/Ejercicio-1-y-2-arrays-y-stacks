# create class for stack
class Stack_int:

	# create empty list
	def __init__(self):
		self.Elements = []
		
	# push() for insert an element
	def push(self, value):
		self.Elements.append(value)
	
	# pop() for remove an element
	def pop(self):
		return self.Elements.pop()
	
	# empty() check the stack is empty of not
	def empty(self):
		return self.Elements == []
	
	# show() display stack
	def show(self):
		print('Current stack: {}'.format(self.Elements))