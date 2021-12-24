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

st=stack()
a=[1,2,3,4,5,6]
for _ in a:
    st.push(_)

print(st.Top())
print(st.pop())
print(st.Top())
print(st.check_empty())
print(st.pop())
print(st.pop())
print(st.pop())
print(st.pop())
print(st.pop())
print(st.pop())
print(st.check_empty())

