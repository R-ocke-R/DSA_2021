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

    def Topele(self):
        if (self.top==-1):
            return 'stack empty'
        return self.stck[self.top]

    def Top(self):
        if (self.top==-1):
            return 'stack empty'
        return self.top

    def insertAtBottom(self,elem):
        if self.check_empty():          # this is a pretty simple function
            self.push(elem)             # what this does is that it pops out the element till the list is empty
            return                      # and then is pushes the new element and this works its way backword pushing
        e = self.pop()                  # the last element which it popped. and then works its way back till the
        self.insertAtBottom(elem)       # top most element
        self.push(e)
        return


    def reverse(self):
        if self.check_empty():
            return
                                        # looks kinda buggy but its a wonderful question and very easy once implemented.
        ele=self.pop()
        self.reverse()
        self.insertAtBottom(ele)
        return

st=stack()
st.push(1)
st.push(2)
st.push(3)
st.push(4)
st.push(5)
print(st.stck)
st.reverse()
print(st.stck)

