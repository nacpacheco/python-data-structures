class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self.value)

class Queue():
    def __init__(self):
        self.length = 0
        self.first = None
        self.last = None

    def __str__(self):
        node_list = []
        current_node = self.first
        while (current_node != None):
            node_dict = {}
            node_dict['value'] = current_node.value
            node_dict['next'] = current_node.next
            node_list.append(node_dict)
            current_node = current_node.next
        node_list.append({'last': self.last, 'first': self.first})
        return str(node_list)

    def peek(self):
        return str(self.first)

    def dequeue(self):
        if self.isEmpty():
            return self
        elif self.length == 1:
            self.first = None
            self.last = None
            self.length -= 1
        else:
            self.first = self.first.next
            self.length -= 1

    def enqueue(self,value):
        new_node = Node(value)
        if self.isEmpty():
            self.first = new_node
            self.last = new_node
            self.length += 1
        else:
            self.last.next = new_node
            self.last = new_node
            self.length += 1

    def isEmpty(self):
        return self.length == 0

queue = Queue()
queue.enqueue('google')
print(queue)
queue.enqueue('udemy')
print(queue)
queue.enqueue('discord')
print(queue)
queue.dequeue()
print(queue)
print(queue.peek())