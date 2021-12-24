# stack = LIFO structure.
# Queue = FIFO structure.

# basically these interchange methods are not
# always very useful, they are there to test whether you
# can do the task of conversion... that's it.

# now there are two to do this question and both ways
# are fairly easy to think/

# remember them as, one with expensive push, one with
# expensive pop, and you can easily make the logic of 
# both in hardly a minute....

# first, expensive pop method.

class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if len(self.queue) == 0:
            return 'empty'
        return self.queue.pop(0)


class stack_expensive_pop:

    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, value):  # cheap/ O(1)
        self.q1.enqueue(value)

    def pop(self):
        if len(self.q1.queue) == 0:
            return 'empty'
        while len(self.q1.queue) != 1:
            self.q2.enqueue(self.q1.dequeue())
        popele = self.q1.dequeue()
        (self.q2.queue, self.q1.queue) = (self.q1.queue, self.q2.queue)
        return popele


s1 = stack_expensive_pop()
(s1.push(1))
(s1.push(2))
(s1.push(3))
(s1.push(4))
print(s1.q1.queue)

print(s1.pop())
print(s1.q2.queue)
print(s1.q1.queue)
print(s1.pop())

(s1.push(5))
print(s1.pop())

print('over')


# now the expensive push method
# reusing the class queue

class stack_expensive_push:

    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, value):
        self.q2.enqueue(value)              # push into the empty q2
        while len(self.q1.queue) != 0:
            self.q2.enqueue(self.q1.dequeue())
        (self.q2.queue, self.q1.queue) = (self.q1.queue, self.q2.queue)
        return

    def pop(self):
        if len(self.q1.queue) == 0:
            return 'empty'
        return self.q1.dequeue()


s2 = stack_expensive_push()
(s2.push(1))
(s2.push(2))
(s2.push(3))
(s2.push(4))
print(s2.q1.queue)

print(s2.pop())
print(s2.q1.queue)
print(s2.pop())
print(s2.q1.queue)

(s2.push(5))
print(s2.pop())
