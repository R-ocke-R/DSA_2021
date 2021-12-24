# disclaimer
# in this implementation i have actually used a linked list
# as a class object, i mainly relied on the insert at end
# and remove at start

# there is also an expectation and need, making this around
# the concept of linked list, without the need of
# its own functions and class
# this is in the linked list concept queue question.

class node:
    def __init__(self,value=None):
        self.data=value
        self.next=None

class linked_list:
    def __init__(self):
        self.head=None

    def insert_at_beginning(self,value):
        n=node(value)
        if self.head==None:
            self.head=n
            return
        n.next=self.head
        self.head=n

    def insert_at_end(self,value):
        n=node(value)
        h=self.head
        if h==None:
            self.head=n
            return
        while h.next!=None:
            h=h.next
        h.next=n


    def remove_at_beginning(self):
        temp=self.head
        self.head=self.head.next
        temp=None

    def printy(self):
        h=self.head
        while h!=None:
            print(h.data)
            h=h.next

    def county(self):
        h=self.head
        c=0
        while h!=None:
            c+=1
            h=h.next
        return c

    def remove_at_end(self):
        h=self.head
        if h==None:
            return
        if h.next==None:
            self.head=None
            return
        while h.next.next!=None :
            h=h.next
        temp=h.next
        h.next=None
        temp=None


ll=linked_list()
ll.insert_at_beginning(2)
ll.insert_at_beginning(1)
ll.insert_at_end(3)
ll.insert_at_beginning(0)
# ll.printy()
ll.remove_at_beginning()
ll.remove_at_end()
ll.remove_at_end()
ll.remove_at_end()
# ll.printy()

class Queue:
    def __init__(self):
        self.queue=linked_list()

    def enqueue(self,value):
        self.queue.insert_at_end(value)

    def dequeue(self):
        self.queue.remove_at_beginning()

    def peek(self):
        return self.queue.head.data

    def empty(self):
        if self.queue.county()==0:
            return True
        return False


Q=Queue()
Q.enqueue(1)
Q.enqueue(2)
Q.enqueue(3)
Q.enqueue(4)
Q.enqueue(5)
Q.queue.printy()
Q.dequeue()
Q.queue.printy()






