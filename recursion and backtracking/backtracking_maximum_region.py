def check(a, ii, jj):
    if  ii>=0 and ii<len(a) and jj>=0 and jj<len(a[0]) and a[ii][jj] == 1:
        return True
    return False


def call_region(i, j):
    global m
    global a
    m.append([i, j])
    a[i][j] = 0
    if check(a, i + 1, j):
        #print('down')
        call_region( i + 1, j)
    if check(a, i, j + 1):
        #print('right')
        call_region( i, j + 1)
    if check(a, i - 1, j):
        #print('up')
        call_region( i - 1, j)
    if check(a, i, j - 1):
        #print('lef')
        call_region( i, j - 1)
    if check(a, i +1, j +1):
        #print('diag')
        call_region( i +1, j+ 1)
    if check(a, i-1, j-1):
        #print('diag')
        call_region(i-1, j-1)

    if check(a, i +1, j- 1):
        #print('diag')
        call_region(i+1, j-1)
    if check(a, i-1, j+1):
        #print('diag')
        call_region(i-1, j+1)

    return

def driver():
    pass


n = 5
a = [[0, 0, 1, 1, 0],
     [1, 0, 1, 1, 0],
     [0, 1, 0, 0, 0],
     [0, 0, 0, 0, 1]]
max_region = 0
m = []
for i in range(len(a)):
    for j in range(len(a[0])):
        if a[i][j] == 0:
            continue
        call_region(i, j)

        if len(m) > max_region:
            max_region = len(m)
        m=[]
print(max_region)

