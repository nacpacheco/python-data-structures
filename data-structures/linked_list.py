class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __str__(self):
        return str(self.__dict__)

class MyLinkedList():
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self.length = 1

    def __str__(self):
        return str(self.__dict__)

    def append(self, value):
        new_node = Node(value)
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
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
        new_node.next = holding_ponter
        self.length += 1
    
    def traverseToIndex(self, index):
        counter = 0
        current_node = self.head
        while (counter != index):
            current_node = current_node.next
            counter += 1
        return current_node

    def remove(self, index):
        if index == 0:
            pos_node = self.head.next
            self.head = pos_node
            self.length -= 1
        elif index >= self.length:
            pre_node = self.traverseToIndex(self.length-2)
            pre_node.next = None
            self.tail = pre_node
            self.length -= 1
        else:
            pre_node = self.traverseToIndex(index-1)
            delete_node = pre_node.next
            pre_node.next = delete_node.next 
            self.length -= 1

    def reverse(self):
        if self.length == 1:
            return self.head
        first = self.head
        self.tail = self.head
        second = first.next
        while (second):
            temp = second.next
            second.next = first
            first = second
            second = temp
        self.head.next = None
        self.head = first

linked_list = MyLinkedList(10)
linked_list.append(15)
linked_list.append(5)
linked_list.prepend(1)
linked_list.insert(2, 99)
print(linked_list.print_list())
linked_list.remove(2)
linked_list.reverse()
print(linked_list.print_list())
