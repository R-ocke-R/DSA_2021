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

    def remove(self, value):
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

    def remve(self,pos):
        if self.head==None:
            return
        if pos==0:
            self.head=self.head.next
        count=1
        temp=self.head.next
        prev=self.head
        while count!=pos and temp!=None:
            count+=1
            prev = temp
            temp=temp.next

        if temp!=None:
            prev.next=temp.next
            temp=None


    def length(self):
        h = self.head
        count=0
        while h != None:
            count+=1
            h = h.next
        return count

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

    def josephus(self,k):
        l=self.length()
        while l!=1:

            if l>=k:
                self.remve(k - 1 )
                self.append_k_nodes_to_start(l-k)
            else:
                self.remve((k-1)%(l))
                #print((k-1)%(l))

            l-=1
            self.printy()
            print()
        return


obj=linked_list()
arr=[5,6,7,8,9,10,1,2,3,4]
arr.reverse()
for i in arr:
    obj.insertAtStart(i)
for i in arr:
    obj.insertAtStart(i)
#obj.printy()
#print()
obj.append_k_nodes_to_start(10)
#obj.printy()
#print()
#obj.josephus(5)

obb=linked_list()
obb.insertAtStart(4)
obb.insertAtStart(3)
obb.insertAtStart(2)
obb.insertAtStart(1)
#obb.printy()
#print()
#obb.josephus(2)


ob=linked_list()
ar=list(range(20,0,-1))
for i in ar:
    ob.insertAtStart(i)
ob.printy()
print()
print(ob.length())
ob.josephus(4)


#obj.(4)
#obj.printy()


