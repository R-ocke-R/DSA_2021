# very basic approach
# we use 2 stacks, you will understand why two are needed.

# enqueue:
# just push the element into 2

# enqueue:
# for pop we need to take the first element out not the
# last (as stack 1 pop will gave us LIFO

# thus we check if stack 2 is empty ** this is important too
# if its empty we pop elements from stack 1 and
# push them in here.

# now they are in reverse order, pop from stack 2 gives us FIFO

# now the important part about why to only pop from 1
# when stack 2 is empty is because.

# suppose st1=(1,2,3,4), st2=()
# -> queue.pop()

# st2=(4,3,2,1), st1= ()
# popele=1, st2 =(4,3,2)

# now push 5
# st2 =(4,3,2), st1=(5)

# now pop()
# now if we take 5 and push to st2, we break the order(FIFO)
# because we get 5 and not 2...





class stack:
    def __init__(self):
        self.top=-1
        self.stck=[]

    def push(self,value):
        # no max/size value
        self.top+=1
        self.stck.append(value)

    def pop(self):
        if self.top==-1:
            return 'stack empty'
        self.top-=1
        return self.stck.pop()

    def check_empty(self):
        if self.top==-1:
            return True
        return False

    def Top(self):
        if (self.top==-1):
            return 'stack empty'
        return self.stck[self.top]


class queue:
    def __init__(self):
        self.st1=stack()
        self.st2=stack()

    def enqueue(self, value):
        self.st1.push(value)
        return

    def dequeue(self):
        if self.st1.check_empty() and self.st2.check_empty():
            return 'empty'
        if self.st2.check_empty():
            while not self.st1.check_empty():
                self.st2.push(self.st1.pop())
        return self.st2.pop()

    def check_empty(self):
        if self.st1.check_empty() and self.st2.check_empty():
            return True
        return False
    
    # now there is also a second approach in dequeue, 
    # like we had in reverse a stack, where once we used 
    # two stack, once we used the call-function stack to
    # append from the bottom.
    
    # similarily here also we use the recersive call-function-stack
    # to pop out the last element (i.e. to pop according to 
    # FIFO, its pretty simple if you think about it clealy.
    
    def recursive_dequeue(self):
        # note right now we just have one stack 
        # we do have st2 but assuming otherwise 

        if self.st1.check_empty():
            return 'emptt'
        if self.st1.top==0:
            return self.st1.pop()
        t=self.st1.pop()
        ele= self.recursive_dequeue()
        self.st1.push(t)
        return ele


    
Q=queue()
print(Q.check_empty())
Q.enqueue(1)
Q.enqueue(3)
Q.enqueue(5)
print(Q.recursive_dequeue())
print(Q.recursive_dequeue())
print(Q.recursive_dequeue())
print(Q.recursive_dequeue())
print(Q.check_empty())
#print(Q.dequeue())
Q.enqueue(7)
print(Q.recursive_dequeue())



QQ=queue()
QQ.enqueue(1)
QQ.enqueue(3)
QQ.enqueue(5)
print(QQ.recursive_dequeue())
QQ.enqueue(7)
print(QQ.recursive_dequeue())
print(QQ.recursive_dequeue())
print(QQ.recursive_dequeue())
print(QQ.recursive_dequeue())





    