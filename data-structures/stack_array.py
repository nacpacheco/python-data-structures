class Stack():
    def __init__(self):
        self.array = []

    def __str__(self):
        return str(self.__dict__)

    def peek(self):
        return self.array[-1]

    def pop(self):
        self.array.pop()

    def push(self,value):
        self.array.append(value)


stack = Stack()
stack.push('google')
stack.push('udemy')
print(stack.peek())
stack.pop()
print(stack)