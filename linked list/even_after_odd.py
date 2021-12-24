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
        return

    def length(self):
        h = self.head
        count=0
        while h != None:
            count+=1
            h = h.next
        return count

    def insertAtStart(self, value):
        n = node(value)
        n.next = self.head
        self.head = n
        return

    def odd_after_even(self):
        o=self.head
        e=self.head.next
        temp=self.head.next
        while e.next!=None and e.next.next!=None:
            o.next=e.next
            o=o.next
            e.next=o.next
            e=e.next
        if e.next!=None:
            o.next=e.next

        o.next=temp
        return

    def even_after_odd(self):
        o=self.head
        e=self.head.next
        temp=self.head.next
        while e.next!=None and e.next.next!=None:
            o.next=e.next
            o=o.next
            e.next=o.next
            e=e.next
        if e.next!=None:
            o.next=e.next
        o.next=None
        e.next=self.head
        self.head=temp
        return





obj=linked_list()
arr=[5,6,7,8,9,10,1,2,3,4]
arr.reverse()
for i in arr:
    obj.insertAtStart(i)

obj.printy()
print()
#obj.odd_after_even()
#obj.printy()
#print()
obj.insertAtStart(20)
obj.printy()
print()
#obj.odd_after_even()
#obj.printy()
#print()

obj.even_after_odd()
obj.printy()
print()




