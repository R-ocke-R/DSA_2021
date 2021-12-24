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

    def insert_when_sorted(self, value):
        n = node(value)
        if self.head == None:
            self.head = n
            return
        h = self.head
        p = h
        while h != None:
            p = h
            h = h.next
            if h != None:
                if h.data >= value:
                    break
        n.next = p.next
        p.next = n
        return

    def remove_with_value(self, value):
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

    def merge_two_sorted_linked_list(self, head2):
        # we use the concepts of sorting
        # two already sorted array, from merge sort
        h1 = self.head  # I dont make (n+m) new node,
                        # just make one new node and
                        # reuse the already made nodes.
        h2 = head2.head  # new sorted list in a new list object.
        n3 = linked_list()
        h3 = node(None)
        n3.head = h3  # asssuming that none is empty
        while h1 != None and h2 != None:
            if h1.data <= h2.data:
                h3.next = h1
                h1 = h1.next
                h3 = h3.next
            else:
                h3.next = h2
                h2 = h2.next
                h3 = h3.next
        if h1 == None:
            while h2 != None:
                h3.next = h2
                h2 = h2.next
                h3 = h3.next

        elif h2 == None:
            while h1 != None:
                h3.next = h1
                h1 = h1.next
                h3 = h3.next
        # n3.head = h3.data
        n3.remove_with_value(n3.head.data)
        return n3


obj = linked_list()
obj.insert_when_sorted(10)
obj.insert_when_sorted(11)
obj.insert_when_sorted(12)
obj.insert_when_sorted(13)
obj.insert_when_sorted(14)
obj.insert_when_sorted(15)
obj.insert_when_sorted(16)
obj.insert_when_sorted(17)
obj.insert_when_sorted(18)
obj.insert_when_sorted(19)
obj.insert_when_sorted(20)
obj.printy()
print()
obb = linked_list()
obb.insert_when_sorted(1)
obb.insert_when_sorted(3)
obb.insert_when_sorted(5)
obb.insert_when_sorted(11)
obb.insert_when_sorted(15)
obb.insert_when_sorted(19)
obb.insert_when_sorted(23)
obb.insert_when_sorted(30)
obb.insert_when_sorted(50)
obb.insert_when_sorted(40)

obb.printy()
print()
o = obj.merge_two_lists_into_the_one_which_calls(obb)
o.printy()
