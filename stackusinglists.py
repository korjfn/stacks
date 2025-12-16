stack = []
# push

stack.append("a")

stack.append("b")

stack.append("c")

print("Stack: " , stack)


# pop

element = stack.pop()
print("Pop: " , element)

# peek

topelement = stack[-1]

print("peek: " , topelement)

# isEmpty

isEmpty = not bool(stack)

print("IsEmpty: " , isEmpty)

# size

print("Size: " , len(stack))

stack.peek()