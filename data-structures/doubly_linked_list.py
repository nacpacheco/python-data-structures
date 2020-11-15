class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
    
    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self.value)

class MyDoublyLinkedList():
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self.length = 1

    def __str__(self):
        node_list = []
        current_node = self.head
        while (current_node != None):
            node_dict = {}
            node_dict['prev'] = current_node.prev
            node_dict['value'] = current_node.value
            node_dict['next'] = current_node.next
            node_list.append(node_dict)
            current_node = current_node.next
        return str(node_list)

    def append(self, value):
        new_node = Node(value)
        new_node.prev = self.tail
        self.tail.next = new_node 
        self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        self.head.prev = new_node
        new_node.next =  self.head
        self.head = new_node
        self.length += 1

    def print_list(self):
        array_list = []
        current_node = self.head
        while (current_node != None):
            array_list.append(current_node.value)
            current_node = current_node.next
        return array_list

    def insert(self, index, value):
        if index >= self.length:
            return self.append(value)
        elif index == 0:
            return self.prepend(value)
        new_node = Node(value)
        leader_node = self.traverseToIndex(index-1)
        holding_ponter = leader_node.next
        leader_node.next = new_node
        new_node.prev = leader_node
        new_node.next = holding_ponter
        holding_ponter.prev = new_node
        self.length += 1
    
    def traverseToIndex(self, index):
        if index >= self.length/2:
            counter = self.length
            current_node = self.tail
            while (counter != index):
                current_node = current_node.prev
                counter -= 1
        else:
            counter = 0
            current_node = self.head
            while (counter != index):
                current_node = current_node.next
                counter += 1 
        return current_node

    def remove(self, index):
        if index == 0:
            pos_node = self.head.next
            pos_node.prev = None
            self.head = pos_node
            self.length -= 1
        elif index >= self.length:
            pre_node = self.traverseToIndex(self.length-1)
            pre_node.next = None
            self.tail = pre_node
            self.length -= 1
        else:
            pre_node = self.traverseToIndex(index-1)
            delete_node = pre_node.next
            pre_node.next = delete_node.next
            pos_node = pre_node.next
            pos_node.prev = pre_node 
            self.length -= 1


linked_list = MyDoublyLinkedList(10)
linked_list.append(15)
linked_list.append(5)
linked_list.prepend(1)
linked_list.insert(2, 99)
print(linked_list.print_list())
print(linked_list)
linked_list.remove(0)
print(linked_list)
print(linked_list.print_list())
