class stack:
    def __init__(self):
        self.top=-1
        self.stck=[]
        # if size constrants are there
        # self.size=n
        # for now
        self.size=10

    def push(self,value):
        if self.size-1==self.top:
            return "stack overflow"
        self.top+=1
        self.stck[self.top]=value

    def pop(self):
        if self.top==-1:
            return 'stack empty'
        self.top-=1

    def check_empty(self):
        if self.top==-1:
            return True
        return False

    def Top(self):
        if (self.top==-1):
            return 'stack empty'
        return self.stck[self.top]
