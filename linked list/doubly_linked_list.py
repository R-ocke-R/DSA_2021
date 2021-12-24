class dnode:
    def __init__(self,value):
        self.data=value
        self.next=None
        self.prev=None

class D_linked_list:
    def __init__(self):
        self.head=None

    def insert_from_start(self,value):
        new=dnode(value)
        if self.head==None:
            self.head=new
            return
        self.head.prev=new
        new.next=self.head
        self.head=new
        return

    def insert_from_end(self,value):
        new=dnode(value)
        if self.head==None:
            self.head=new
            return
        h=self.head
        while h.next!=None:
            h=h.next
        h.next=new
        new.prev=h

    def printy(self):
        if self.head==None:
            return
        h=self.head
        while h!=None:
            print(h.data,end=' ')
            h=h.next

    def remove(self,value):
        if  self.head==None:
            return
        if self.head.data==value:
            self.head=self.head.next
            self.head.prev=None
            return
        h=self.head.next
        while h!=None:
            if h.data==value:
                if h.next==None:
                    # this is the edge case
                    h.prev.next=None
                    h=None
                    return
                h.prev.next=h.next
                h.next.prev=h.prev
                h=None
                return
            h=h.next
        return



obj=D_linked_list()
aa=list(range(5))
bb=list(range(3,9))
for i in aa:
    obj.insert_from_end(i)
obj.printy()
print()
for i in bb:
    obj.insert_from_start(i)
obj.printy()
print()
obj.remove(4)
obj.remove(4)
obj.remove(3)
obj.remove(3)
obj.printy()
print()

