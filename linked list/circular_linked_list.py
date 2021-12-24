class cnode:
    def __init__(self, value):
        self.data = value
        self.next = None


class C_linked_list:
    def __init__(self):
        self.head = None

    def insertAtEnd(self,value):
        new=cnode(value)
        if self.head==None:
            self.head=new
            new.next=self.head
            return
        h=self.head
        while h.next!=self.head:
            h=h.next
        h.next=new
        new.next=self.head
        return

    def insertAtStart(self,value):
        new=cnode(value)
        if self.head==None:
            self.head=new
            new.next=self.head
            return
        h = self.head
        while h.next != self.head:
            h = h.next
        new.next=self.head
        h.next=new
        self.head = new
        return

    def printy(self):
        if self.head==None:
            return
        h=self.head
        while h.next!=self.head:
            print(h.data,end=' ')
            h=h.next
        print(h.data,end=' ')
        return

    def removeAtTop(self):
        temp=self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next=self.head.next
        self.head=None
        self.head=temp.next

    def remove(self, pos):
        if pos==1:
            self.removeAtTop()
            return
        count=1
        temp=self.head

        while count !=pos:
            temp=temp.next
            count+=1
        to_del=temp.next
        temp.next=temp.next.next
        return

    def insert_middle(self,value):
        #this is exactly the same as that of single linked list

        pass


obj=C_linked_list()
ar=list(range(1,5))
for i in ar:
    obj.insertAtEnd(i)
obj.printy()
print()
ar=list(range(8,10))
for i in ar:
    obj.insertAtStart(i)
obj.printy()
print()
obj.removeAtTop()
obj.printy()
print()