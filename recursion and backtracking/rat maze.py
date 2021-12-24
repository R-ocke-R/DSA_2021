# from deepcopy import copy
def check(a, i, j, direction, solur):
    if direction == 'd' and i + 1 < len(a) and a[i + 1][j] == 1 and solur[i+1][j] == 0:
        return True
    if direction == 'r' and j + 1 < len(a[0]) and a[i][j + 1] == 1 and solur[i][j+1] == 0:
        return True
    if direction == 'l' and j - 1 >= 0 and a[i][j - 1] == 1 and solur[i][j-1] == 0:
        return True
    if direction == 'u' and i - 1 >= 0 and a[i - 1][j] == 1 and solur[i-1][j] == 0:
        return True


def backtracking(ar, i, j, n, stacky, finalstack, solar):
    global county               # similarily can make other parameters as global variable
    county+=1                   # and  make returning and calling of functions easier.
    if i == n - 1 and j == n - 1:
        finalstack.append(stacky[:])
        for i in range(n):
            print(solar[i])
        return stacky, finalstack , solar

    if check(ar, i, j, 'd', solar):
        solar[i+1][j]=1
        stacky.append('D')
        (stacky, finalstack, solar) = backtracking(ar, i + 1, j, n, stacky, finalstack,solar)
        solar[i+1][j]=0
        stacky.pop()

    if check(ar, i, j, 'r', solar):
        solar[i][j + 1] = 1
        stacky.append('R')
        (stacky, finalstack, solar) = backtracking(ar, i, j + 1, n, stacky, finalstack,solar)
        stacky.pop()
        solar[i][j+1] = 0

    if check(ar, i, j, 'l',solar):
        solar[i][j - 1]=1
        stacky.append('L')
        (stacky, finalstack, solar) = backtracking(ar, i, j - 1, n, stacky, finalstack, solar)
        stacky.pop()
        solar[i][j - 1] = 0

    if check(ar, i, j, 'u', solar):
        solar[i-1][j] = 1
        stacky.append('U')
        (stacky, finalstack, solar) = backtracking(ar, i-1, j , n, stacky, finalstack, solar)
        stacky.pop()
        solar[i-1][j] = 0

    return stacky, finalstack, solar


n = 4
arr = [[1, 0, 0, 0],
       [1, 1, 0, 1],
       [1, 1, 0, 0],
       [0, 1, 1, 1]]
county=0
stack = []
finals = []
solarr=[[0 for i in range(n)] for j in range(n)]


if arr[0][0] == 0:
    print('Rat died already')
else:
    solarr[0][0] = 1
    (a, b, c) = backtracking(arr, 0, 0, n, stack, finals,solarr)
    for i in range(len(finals)):
        finals[i] = ''.join(finals[i])
    finals.sort()
    print(b)
    print(county)
