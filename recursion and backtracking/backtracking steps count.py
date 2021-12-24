def stepCheck(ele,stck,n):
    if sum(stck) + ele <= n:
        return True
    return False

def stepbcktrack(n):
    global final, stck

    if sum(stck) == n:
        final.append(stck[:])
        return
    if stepCheck(1, stck,n):
        stck.append(1)
        stepbcktrack(n)
        stck.pop()
    if stepCheck(2,stck,n):
        stck.append(2)
        stepbcktrack(n)
        stck.pop()
    if stepCheck(3,stck,n):
        stck.append(3)
        stepbcktrack(n)
        stck.pop()
    return


def stepPerms(n):
    # the common way might not be backtracking but its a 'obvious' thing that comes to mind.
    # other way is calculate recursively, for each , like the coin change?
    global final
    stepbcktrack(n)
    return len(final) % 10000000007

final=[]
stck=[]

stepbcktrack(5)
print(final)
print(len(final))