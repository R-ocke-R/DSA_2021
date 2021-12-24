class node:
    def __init__(self,value):
        self.data=value
        self.next=None

class queue:
    def __init__(self):
        self.back=None
        self.front=None

    def enqueue(self,value):
        n=node(value)
        if self.front==None:
            self.front=n
            self.back=n
            return

        self.back.next=n
        self.back=n

    def dequeue(self):
        if self.front==None:                      #  or self.back.next==self.front: we dont need to check this coz, even in this case self.front will point to NOne
            return -1
        temp=self.front
        self.front=self.front.next
        temp=None

    def empty(self):
        if self.front==None:
            return True
        return False

    def peek(self):
        if self.front==None:
            return -1
        return self.front.data


Q=queue()
Q.enqueue(1)
Q.enqueue(2)
Q.enqueue(3)
Q.enqueue(4)
print(Q.peek())
Q.dequeue()
print(Q.empty())
print(Q.peek())
Q.dequeue()
print(Q.peek())
Q.dequeue()
print(Q.peek())
Q.dequeue()
print(Q.empty())







