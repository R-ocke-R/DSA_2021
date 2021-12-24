class node:
    def __init__(self, value):
        self.data = value
        self.next = None


class linked_list:
    def __init__(self):
        self.head = None

    def printy(self):
        h = self.head
        while h != None:
            print(h.data, end=' ')
            h = h.next

    def insertAtStart(self, value):
        n = node(value)
        n.next = self.head
        self.head = n

    def insertAtEnd(self, value):
        n = node(value)
        if self.head is None:
            self.head = n
            return
        h = self.head
        while h.next != None:
            h = h.next
        h.next = n

    def insertInMiddle(self,value,middle_node):
        # here the middle node is already provided
        # so it doesn't need to be calculated...
        pass

    def insert_when_sorted(self, value):
        n = node(value)
        if self.head==None:
            self.head=n
            return
        h=self.head
        p=h
        while h != None:
            p=h
            h=h.next
            if h!= None:
                if h.data>=value:
                    break
        n.next = p.next
        p.next = n

        return

    def remove_with_value(self, value):
        if self.head == None:
            return
        h = self.head
        if h.data == value:
            self.head = h.next
            h = None
            return
        prev = self.head
        h = self.head.next
        while h != None:
            if h.data == value:
                break
            prev = h
            h = h.next
        if h == None:
            return

        prev.next = h.next
        h = None


listob=linked_list()
listob.insert_when_sorted(4)
listob.printy()
print()
listob.insertAtStart(3)
listob.insertAtStart(2)
listob.insertAtStart(1)
listob.insertAtEnd(5)
listob.insertAtEnd(6)
listob.printy()
print()
listob.insert_when_sorted(4)
listob.insert_when_sorted(7)
listob.insert_when_sorted(1)
listob.printy()