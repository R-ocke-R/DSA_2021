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
            h=f.next            #h is just a refrence to store the next address
            f.next=p            #basically its the f which goes till the end.
            p=f                 #p stores the 'now' current ele, which will be the prev for next iter
            f=h
        self.head=p

    #def recursive_reverse(self):



listob=linked_list()
listob.insertAtStart(6)
listob.insertAtStart(5)
listob.insertAtStart(4)
listob.insertAtStart(3)
listob.insertAtStart(2)
listob.insertAtStart(1)
listob.printy()
print()
listob.reverse_the_list()
print(listob.head)
listob.printy()
print()
