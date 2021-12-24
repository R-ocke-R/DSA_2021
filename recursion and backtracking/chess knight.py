def check(i, j):
    global ar
    if 0 <= i <= 7 and 0 <= j <= 7 and ar[i][j] == False:
        return [i, j]
    return False

def chess_knight(i, j):
                                # there are 8 movements available.
    global ar                   # returns a list of position where its going next, or else return false.
    global count
    ii = [+2, +1, -1, -2, -2, -1, +1, -2]
    jj = [+1, +2, +2, +1, -1, -2, -2, -1]
    ar[i][j]=count
    count+=1
    for k in range(8):
        iii=i+ii[k]
        jjj=j+jj[k]
        c=check(iii, jjj)
        if c != False:
            chess_knight(c[0],c[1])

i = 0
j = 0
n = 8                                                       # making this one fixed with n=8
ar = [[False for m in range(n)] for p in range(n)]
count=0
chess_knight(i,j)
print(ar)