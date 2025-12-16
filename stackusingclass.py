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



mystack = Stack()
mystack.push('a')
mystack.push('b')
mystack.push('c')


print("stack:", mystack.stack)
print("pop", mystack.pop())
print("stack:", mystack.stack)
print("peek", mystack.peek())
print("IsEmpty", mystack.isEmpty())
print("Size", mystack.size())