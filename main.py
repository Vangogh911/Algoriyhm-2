import random


class Node:
    def __init__(self, val=None):
        self.val = val
        self.nextVal = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_end(self, newVal):
        newNode = Node(newVal)
        if self.head is None:
            self.head = newNode
            return
        lastNode = self.head
        while lastNode.nextVal:
            lastNode = lastNode.nextVal
        lastNode.nextVal = newNode

    def show_nodes(self):
        lastNode = self.head
        while lastNode.nextVal:
            print(lastNode.val)
            lastNode = lastNode.nextVal
        print(lastNode.val)

    def reverse_list(self, tail=None):
        lastNode = self.head
        lastNode.nextVal, tail = tail, lastNode.nextVal
        while tail.nextVal:
            tail.nextVal, tail, lastNode = lastNode, tail.nextVal, tail
        tail.nextVal = lastNode
        self.head = tail
        print("List reversed")


test = LinkedList()
for i in range(10):
    x = random.randint(0, 100)
    test.add_to_end(x)

test.show_nodes()

print("###############################")

test.reverse_list()

print("###############################")

test.show_nodes()
