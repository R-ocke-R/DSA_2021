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
            print(h.data)
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


class stack:
    def __init__(self):
        self.l=linked_list()
    def pop(self):
        self.l.remove(self.l.head.data)
    def push(self,valu):
        self.l.insertAtStart(valu)
    def printAll(self):
        self.l.printy()

st=stack()
st.push(5)
st.push('monday')
st.push(20)
st.printAll()
st.pop()
st.printAll()

# now in basic steps we made a stack of off a
# linked list class
# though we could also use inheritance
# i didnt find it quite necessary and its
#  better to have both excluded. maybe...


# also cna make for size, which could be a copy
# of printy replaced with count
# and count make top value peek fucntion by
# simply printing the self.l.head.value