# def delnodes(m, n, head):
#     while head.next != None:
#         print(head.value)
#         head = head.next
#
# class Node(object):
#     def __init__(self, value):
#         self.value = value
#         self.nextnode = None
#
# a = Node(1)
# b = Node(2)
# c = Node(3)
# d = Node(4)
# e = Node(5)
#
# a.nextnode = b
# b.nextnode = c
# c.nextnode = d
# d.nextnode = e
#
# while head.next != None:
#     print(head.value)
#     head = head.next
class LinkedList:
    def __init__(self, values=None):
        self.head = None
        self.tail = None
        if values is not None:
            self.add_multiple_nodes(values)
    def __str__(self):
        return ' -> '.join([str(node) for node in self])
    def __len__(self):
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next
        return count
    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next
    @property
    def values(self):
        return [node.value for node in self]
    def add_node(self, value):
        if self.head is None:
            self.tail = self.head = Node(value)
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return self.tail
    def add_multiple_nodes(self, values):
        for value in values:
            self.add_node(value)
    def add_node_as_head(self, value):
        if self.head is None:
            self.tail = self.head = Node(value)
        else:
            self.head = Node(value, self.head)
        return self.head