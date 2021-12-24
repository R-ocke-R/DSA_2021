def braces(A):
    n=len(A)
    sop=[]
    srp=[]
    operators=['+','-','/','*']
    i=0
    while i<n:
        if A[i]=='(':
            sop.append('1')
            i+=1
        elif A[i] in operators:
            sop.append('o')
            i+=1
        elif A[i]==')':
            if len(sop)==0 or sop[-1]=='1':
                return 1
            while sop[-1]!='1':
                sop.pop()
            sop.pop()
            i+=1
        else:
            i+=1
    return 0

print(braces('(a+(a+b))'))