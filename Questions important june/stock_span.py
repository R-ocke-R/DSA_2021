# read question from DSA narisimma page 195

# code for class stack
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


# brute approach
def brute(arr):
    span = []
    for i in range(len(arr)):
        j = i - 1
        span.append(1)
        while j != -1 and arr[j] <= arr[i]:
            j = j - 1
            span[i] += 1

    return span

print('brute')
print(brute([6, 3, 4, 5, 2]))
print(brute([7, 5, 4, 6, 8, 5, 3, 1, 4]))


# this approach has two loops, for --> n times and while --> 1+2+3...n --> O(n^2)
# COMBINING--> n+(n+1)+(n+2)...(n+n)--> common--> n[(n^2)]---> n^2 or n^3 ??


# O(n) approach using stack
# this approach dwells on what the last algorithm didn't, in the question span increases if next element increase
# else the span decrease...

# thus we use a stack to store index of elements with increasing order till we encounter
# an element whose value is decreasing then we empty out the stack irrespective of the value
# of any or all elements because once graph has a decrease the span is resetted

def stock_span_stack(arr):
    n = len(arr)
    span = [1 for i in range(n)]
    st = stack()
    st.push(0)

    for i in range(1, n):
        #print(st.stck, arr[i], i)
        if arr[i] < arr[st.Top()]:
            st.push(i)
            continue
        else:
            while not st.check_empty() and arr[i]>=arr[st.Top()]:
                st.pop()
            if st.check_empty():
                p=-1
            else:
                p=st.Top()
            span[i]=i-p
            st.push(i)
    return span
        #if arr[i] == arr[i - 1]:
        #   span[i]=span[i-1]+1
        #    continue
        #if arr[i] > arr[i - 1]:         # if its greater then maybe its greater than even i-2, i-3 and so on, thus while loop
            #while not st.check_empty() and arr[i] > arr[st.Top()]:
                #print('while loop', st.stck,span)
                # case 1: strictly decreasing
                #span[i]+=span[st.Top()]
                #st.pop()

                #j=st.Top()
                ##st.pop()
                #if arr[st.Top()]>arr[j]:
                #    span[j]=1
                #else:
                #    span[j]=

                #if j == st.Top():
                #    span[j] = 1
                #    st.pop()
                #    j=st.Top()

                # case 2: equal
                #else:  # j!=st.Top()
                #    span[j] = i - st.Top()
                #    j -= 1


print('stack')
print(stock_span_stack([6, 3, 4, 5, 2]))
print(stock_span_stack([7, 5, 4, 6, 8, 5, 3, 1, 4]))

# for i in range(1, n):
# print(i)
#    if arr[i] >= arr[i - 1]:
#        span[i] = span[i-1]+1

#    else:
#        span[i]=1
# now we compute and store the value of span in span list.
# s=span[-1]
# while len(st) != 0:
#    print(st[-1], i )
#    span[st[-1]] = i - st[-1]
#    st.pop()
# st.append(s)
# return span
