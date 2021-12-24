class Queue:
    def __init__(self):
        self.front=-1
        self.back=-1
        self.Q=[]
    def enqueue(self,value):            # happends from backend.
        # to empty and new
        if self.front==self.back==-1:
            self.front+=1
            self.back+=1
            self.Q.append(value)
        # to full.
        # here it can't really be full. coz of dynamic structure
        # otherwise we check if self.back==n-1
        else:
            self.back+=1
            self.Q.append(value)
    def dequeue(self):
        if self.front>self.back or self.front==-1:
            return "empty"
        self.front+=1

    def peek(self):
        if self.front>self.back or self.front==-1:
            return "empty"
        return self.Q[self.front]

    def empty(self):
        if self.front>self.back or self.front==-1:
            return True
        return False


queue=Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)


print(queue.peek())
queue.dequeue()
print(queue.peek())
queue.dequeue()
print(queue.empty())
queue.enqueue(6)
queue.dequeue()
queue.dequeue()
print(queue.empty())
queue.dequeue()
queue.dequeue()
print(queue.empty())




