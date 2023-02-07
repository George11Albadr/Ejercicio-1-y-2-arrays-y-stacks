from stack import Stack
from stack_int import Stack_int

# Stack initialization
stack = Stack(5)
print(stack)

# Push first element
stack.push('A')

# Other pushes
stack.push('B')
print(stack)
stack.push('C')
print(stack)
stack.push('D')
print(stack)
stack.push('E')
print(stack)
stack.push(('F'))
print(stack)
# stack.push('F') # Forces stack overflow

# Pops
stack.pop()
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)
# stack.pop() # Forces stack underflow

# Peek
stack.push('D')
stack.push('C')
print(stack)
print('Peek: ', stack.peek())
stack.push('E')
print(stack)
print('Peek: ', stack.peek())


def BottomInsert(s, value):

	# check the stack is empty or not
	if s.empty():
		
		# if stack is empty then call
		# push() method.
		s.push(value)
		
	# if stack is not empty then execute
	# else block
	else:
		popped = s.pop()
		BottomInsert(s, value)
		s.push(popped)

# Reverse() reverse the stack
def Reverse(s):
	if s.empty():
		pass
	else:
		popped = s.pop()
		Reverse(s)
		BottomInsert(s, popped)
  
stk = Stack_int()

stk.push(1)
stk.push(2)
stk.push(3)
stk.push(4)
stk.push(5)

print("Original Stack")
stk.show()

print("\nStack after Reversing")
Reverse(stk)
stk.show()
