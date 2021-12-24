def brute(arr):
    n=len(arr)
    #there are many good brute force approaches available,
    # i'ma go with making a left max and a right max array
    left_max=[]
    right_max=[]
    # note the left_max of first and last_max of last element both are 0
    #left_max.append(0)
    # right_max.append(0)
    for i in range(1,n):
        #print(arr[:i])

        left_max.append(max(arr[:i]))
        right_max.append(max(arr[i:]))


    for i in range(n):
        pass

    print(left_max)
    print(right_max)


brute([0,1,0,2,1,0,1,3,2,1,2,1])
