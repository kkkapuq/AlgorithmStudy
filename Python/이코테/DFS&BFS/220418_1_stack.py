stack = []

stack.append(5)
stack.append(3)
stack.append(4)
stack.pop()
stack.pop()
stack.append(6)
stack.append(7)
stack.pop()

print(stack)
print(stack[::-1])