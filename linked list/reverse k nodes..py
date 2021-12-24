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

    def reverse_the_list(self):
        if self.head==None:
            return
        if self.head.next==None:
            return
        f=self.head
        p=None
        while f!=None:
            h=f.next
            f.next=p
            p=f
            f=h
        self.head=p

    def reverse_k_nodes(self, head, k):
        p = None
        f = head
        h = None
        count = 0

        while f != None and count != k:
            h = f.next
            f.next = p
            p = f
            f = h
            count += 1

        if f != None:
            head.next = self.reverse_k_nodes(h, k)

        return p









listob=linked_list()
listob.insertAtStart(6)
listob.insertAtStart(5)
listob.insertAtStart(4)
listob.insertAtStart(3)
listob.insertAtStart(2)
listob.insertAtStart(1)
listob.printy()
print()
# listob.reverse_the_list()
# listob.printy()
# print()
listob.head=listob.reverse_k_nodes(listob.head,3)
listob.printy()
print()