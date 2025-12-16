class Stack:
    def __init__(self):
        self.stack = []


    def push(self,element):
        self.stack.append(element)

    def pop(self):
        if self.isEmpty():
            return "Stack is empty" 
        return self.stack.pop()
    
    def peek(self):
        if self.isEmpty():
            return "Stack is empty" 
        return self.stack[-1]
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    
S = Stack()
S.push(5)
print(S.stack)
S.push(12)
print(S.stack)
S.push(7)
print(S.stack)
print(S.pop())
print(S.stack)
S.push(9)
print(S.stack)
print(S.peek())
print(S.stack)
S.push(3)
print(S.stack)
print(S.pop())
print(S.stack)
print(S.pop())
print(S.stack)
print(S.isEmpty())
print(S.stack)
print(S.pop())
print(S.stack)
print(S.isEmpty())
print(S.stack)