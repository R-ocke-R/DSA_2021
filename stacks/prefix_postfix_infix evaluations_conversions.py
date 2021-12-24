class stack:
    def __init__(self):
        self.top = -1
        self.stck = []

    def push(self, value):
        # no max/size value
        self.top += 1
        self.stck.append(value)

    def pop(self):
        if self.top == -1:
            return 'stack empty'
        self.top -= 1
        return self.stck.pop()

    def check_empty(self):
        if self.top == -1:
            return True
        return False

    def Top(self):
        if (self.top == -1):
            return 'stack empty'
        return self.stck[self.top]

    def prefix_evaluation(self,str):
        for i in str[::-1]:
            if i.isdigit():
                self.push(int(i))
            else:
                op1=self.pop()
                op2=self.pop()
                if i=='+':
                    self.push(int(op1+op2))
                    continue
                if i=='-':
                    self.push(int(op1-op2))
                    continue
                if i=='/':
                    self.push(int(op1/op2))
                    continue
                if i=='*':
                    self.push(int(op1*op2))
                    continue
        return self.pop()

    def postfix_evaluation(self,str):
        for i in str:
            if i.isdigit():
                self.push(int(i))
            else:
                op2=self.pop()              # note this change in the first pop and the second
                op1=self.pop()              # the first pop is the right-sided operand.
                # print(op1,op2)
                if i=='^':                  # this here is the exponential operator,
                    self.push(int(op1 ** op2))# coz cant really use ** as they are two character
                    continue                # simple alternate,
                                            # is to use string.replace to the input and change "**" to '^'
                if i=='+':
                    self.push(int(op1+op2))
                    continue
                if i=='-':
                    self.push(int(op1-op2))
                    continue
                if i=='/':
                    self.push(int(op1//op2))
                    continue
                if i=='*':
                    self.push(int(op1*op2))
                    continue
        return self.pop()

    def precedence(self,op):
        # **        first
        # * / // %  second
        # + -       third

        if op=='^':
            return 3
        if op=='*' or op=='/':
            return 2
        if op=='+' or op=='-':
            return 1
        return 'error'

    def infix_to_postfix(self,str):
        rev=''
        for i in str:
            if i=='(':
                self.push('(')
            elif i.isalpha():
                rev+=i
            elif i==')':
                while not self.check_empty() and self.Top()!='(':
                        rev+=self.pop()
                if not self.check_empty():      # this to remove the parenthesis open wala
                    self.pop()
            else:         # operator
            # solve one infix to postfix expression without parenthesis to know which, why, what to pop and not to pop
                while not self.check_empty() and self.Top()!='(':
                    if self.precedence(self.Top()) >= self.precedence(i):
                        rev+=self.pop()
                    else:
                        break  # the while loop works tillwe have higher or equal precedence i.e
                                # the if loop works but when condition falls we break out and stop poping shit
                self.push(i)
        while not self.check_empty():
            rev+=self.pop()
        return rev


    def infix_to_prefix(self,str):          # described this algorithim in OneNote
        rev=''
        for i in str[::-1]:
            if i=='(':
                rev+=')'
            elif i==')':
                rev+='('
            else:
                rev+=i
        rev=self.infix_to_postfix(rev)
        rev=rev[::-1]
        return rev



st = stack()
a = [1, 2, 3, 4, 5, 6]
# strung='-+7*45+20'
# print(st.prefix_evaluation(strung))
# strung='46+2/5*7+'
# print(st.postfix_evaluation(strung))
s='a+b*c/d^e-f'
print(s)
#print(st.infix_to_postfix('a+b*c/d^e-f'))                  # note ^ this means xor for operator but since i can't use                                                             # ** in string, (it won't work) so replcing the symbo
print(st.infix_to_postfix(s))



print(st.infix_to_prefix('(a-b/c)*(a/k-l)'))