class Stack(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

s = Stack()


s.push("Hello")
print(s.peek())
s.push(1)
print(s.peek())
s.push(True)
print(s.peek())

print(s.pop())
print(s.pop())
print(s.pop())

print(s.isEmpty())


