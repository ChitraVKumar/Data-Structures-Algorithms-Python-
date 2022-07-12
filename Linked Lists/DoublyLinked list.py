class DoublyLinkedNode(object):
    def __init__(self, value):
        self.value = value
        self.nextnode = None
        self.prevnode = None

a = DoublyLinkedNode(1)
b = DoublyLinkedNode(2)
c = DoublyLinkedNode(3)

a.nextnode = b
b.prevnode = a

b.nextnode = c
c.prevnode = b

