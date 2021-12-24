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

    def floyd_loop_check(self):
        slow = self.head
        fast = self.head
        while slow!=None and fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True

        return False


    def make_loop(self,pos):                # takes the next of the last index and point it to pos
        if self.head==None:                               # thus making a cycle
            return 0
        h=self.head
        count=0                   #my linked list is 1 based indexed.
        temp=None
        last=None
        while h != None:
            count+=1
            if count==pos:
                temp = h
            last = h
            h = h.next

        last.next = temp
        return count

    def remove_loop(self):
        if self.floyd_loop_check():
            slow = self.head
            fast = self.head
            while slow != None and fast != None and fast.next != None:
                slow = slow.next
                fast = fast.next.next
                if slow == fast:
                    fast=self.head
                    while slow.next!=fast.next:
                        fast=fast.next
                        slow=slow.next
                    slow.next =None
                    return

        return False




lis=linked_list()
#lis.insertAtStart(13)
lis.insertAtStart(10)
#lis.insertAtStart(14)
#lis.insertAtStart(15)
lis.insertAtStart(11)
lis.insertAtStart(12)
lis.insertAtStart(13)
lis.printy()
print(lis.floyd_loop_check())
lis.make_loop(2)
print(lis.floyd_loop_check())
lis.remove_loop()
lis.printy()
