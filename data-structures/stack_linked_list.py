class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self.value)

class Stack():
    def __init__(self):
        self.length = 0
        self.top = None
        self.bottom = None

    def __str__(self):
        node_list = []
        current_node = self.top
        while (current_node != None):
            node_dict = {}
            node_dict['value'] = current_node.value
            node_dict['next'] = current_node.next
            node_list.append(node_dict)
            current_node = current_node.next
        node_list.append({'bottom': self.bottom, 'top': self.top})
        return str(node_list)

    def peek(self):
        return str(self.top)

    def pop(self):
        if self.isEmpty():
            pass
        elif self.length == 1:
            self.top = None
            self.bottom = None
            self.length -= 1
        else:
            holding_pointer = self.top
            self.top = self.top.next
            self.length -= 1

    def push(self,value):
        new_node = Node(value)
        if self.isEmpty():
            self.bottom = new_node
            self.top = new_node
            self.length += 1
        else:
            holding_pointer = self.top
            self.top = new_node
            self.top.next = holding_pointer
            self.length += 1

    def isEmpty(self):
        return self.length == 0

stack = Stack()
stack.push('google')
stack.push('udemy')
print(stack)