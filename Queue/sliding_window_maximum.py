from collections import deque


def sliding_window_maximum(nums, k):
    arr = []
    q = deque()
    for i in range(k):
        # 0 to k-1 indexes
        e=nums[i]
        while len(q)!=0 and e>=nums[q[-1]]:         # the number should be greater than to make it pop
            q.pop()                                 # and check till list empty
        q.append(i)                                 # pushing the index
    # print(q)
    print(nums[q[0]], end=' ')

    # that was for first k
    # now the rest nums

    for i in range(k,len(nums)):

        e=nums[i]
        # removing the extra old index if it exist.
        if len(q)!=0 and q[0]<i-k+1:
            q.popleft()

        while len(q)!=0 and e>=nums[q[-1]]:
            q.pop()
        q.append(i)

        print(nums[q[0]],end=' ')


    return arr


num = list(map(int, input().split()))
k = int(input())
sliding_window_maximum(num, k)