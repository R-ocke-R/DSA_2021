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
        print(h.data)
        return

    def leng(self):
        count = 0
        if self.head==None:
            return count
        h=self.head
        while h.next!=self.head:
            count+=1
            #print(h.data,end=' ')
            h=h.next
        #print(h.data,end=' ')
        count += 1
        return count

    def removeAtTop(self):
        temp=self.head
        while temp.next != self.head:
            temp = temp.next
        second=self.head.next
        temp.next=second
        self.head=None
        self.head=second

    def remove(self, pos):
        l=self.leng()
        if pos>=l:
            return
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

    def josephus_last_man(self, m):
        h=self.head
        l=self.leng()
        #l=15
        while l!=1:
            for _ in range(m-2):
                h=h.next
            if h.next==self.head:
                self.removeAtTop()
            else:
                h.next=h.next.next
            h=h.next
            l=l-1
            self.printy()


        print('done')
        #self.leng()
        #self.printy()







obj=C_linked_list()
ar=list(range(1,21))
for i in ar:
    obj.insertAtEnd(i)
obj.printy()
print(obj.leng())


obj.josephus_last_man(4)
#obj.printy()