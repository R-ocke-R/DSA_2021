# code for stack class
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


# the brute force approach:
def brute(hist):
    lar = 0
    n = len(hist)
    for i in range(n):
        mini = hist[i]
        for j in range(i, n):
            mini = min(mini, hist[j])
            lar = max(lar, mini * (j - i + 1))

    return lar


# brute is slow. why?
# because it doesnt rememeber where the rectangle of
# specific height started..

# now the improved solution, uses two basic logics,
# one, each new bar posseses the potential of starting
# a new rectangle of its own height
# now to know the end of that height we gotta
# traverse till we hit something smaller

# now using this we save the heights ('new heights')
# and the positions where they must have started in a very beautiful way
# if we hit a larger element/bar,
# it can form a bigger rectangle from that position to x forward position
# but not with earlier positon

# but if we hit something smaller than the bars,
# we should note that if can form a rectangle
# from that position to x forward (if forward can include it )
# and also behind bars, since they were smaller...


def largest_rectangle_histogram(hist):
    pos_stack = stack()
    bar_stack = stack()
    n = len(hist)
    lar = 0
    for i in range(n):
        store = i       # this is very crucial, coz we store i here for cases
                        # where hist[i] is bigger but
                        # when its not, this store changes itself to the pos_stack.Top()
                        # of the last element popped
                        # thus maintains the intitial pos for the smaller element.

        while not bar_stack.check_empty() and hist[i] < bar_stack.Top():
            # while loop to pop the elements that are smaller and also calculating there area.

            store = pos_stack.Top()
            lar = max(lar, (bar_stack.pop() * (i - pos_stack.pop())))

        if bar_stack.check_empty() or hist[i] > bar_stack.Top():
            pos_stack.push(store)
            bar_stack.push(hist[i])
    return lar


print(brute([6, 2, 5, 4, 5, 1, 6]))
print(largest_rectangle_histogram([2, 3, 4, 4, 1, 2, 4, 0]))
print(largest_rectangle_histogram([6, 2, 5, 4, 5, 1, 6]))
print(largest_rectangle_histogram([2, 4]))
