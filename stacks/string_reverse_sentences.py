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


str = input()
str.strip()
str += ' '                          # to append the last word into the stack

stack = stack()                     # stack object.
word = ''
c = 0

for i in str:
    if i != ' ':
        word += i
    elif word != '':                # this condition checks for the extra spaces in the middle of the sentence.
        stack.push(word)
        word = ''

for i in range(stack.top + 1):
    print(stack.pop(), end=' ')
