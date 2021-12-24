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

    def append_k_nodes_to_start(self, k):
        l=self.length()
        if l<=k:
            return
        c=0
        h=self.head
        while h!=None and c!=l-k-1:
            h=h.next
            c+=1

        endptr=h

        while h.next!=None:
            h=h.next
        h.next=self.head
        self.head=endptr.next
        endptr.next=None

        return

obj=linked_list()
arr=[5,6,7,8,9,10,1,2,3,4]
arr.reverse()
for i in arr:
    obj.insertAtStart(i)
for i in arr:
    obj.insertAtStart(i)
obj.printy()
print()
obj.append_k_nodes_to_start(5)
obj.printy()
print()