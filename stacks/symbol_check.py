class stack:
    def __init__(self):
        self.top = -1
        self.stck = []

    def push(self, value):
        self.stck.append(value)
        self.top += 1
        return

    def pop(self):
        if self.top == -1:
            return False
        self.top -= 1
        return self.stck.pop()

    def check_empty(self):
        if self.top == -1:
            return True
        return False


# this question is modifiable
# i am making it for ( { [  ] } )
str = input()
symbols = {'(': ')', '{': '}', '[': ']'}
stack=stack()
error=0
for i in str:
    if i in symbols.keys():
        stack.push(i)

    if i in symbols.values():
        if i == symbols[stack.pop()]:
            continue
        else:
            error=1
            break
if not stack.check_empty() and error==1:
    print('error')
else:
    print('voila')
