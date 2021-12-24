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

str=input()
leng=len(str)
stack=stack()
revstr=''
for i in str:
    stack.push(i)
for i in range(leng):
    # print(stack.pop())          # to print each character directly in seperate line
    # print(stack.pop(), end='')  # to print each character directly in the same line
    revstr+=stack.pop()
print(revstr)