from queue import Queue

class TreeNode:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

def inorder(root):
    if root==None:
        return
    # Inorder means -> left then root then right
    inorder(root.left)
    print(root.data, end= '->')
    inorder(root.right)
    return


def level_order(root):
    if root == None:
        return
    q = []  # queue
    q.append(root)
    while len(q) != 0:
        t = q[0]
        print(t.data, end='->')
        q = q[1:]  # this operation has O(n) complexity... making the function's O(N^2)
        # use a linked list based deque from collections library to be able to get O(1) popleft.
        if t.left != None:
            q.append(t.left)
        if t.right != None:
            q.append(t.right)

    return


def sum_at_Kth_level(root, k):
    if root == None:
        return
    if k == 0:
        return root.data
    q = []  # queue
    q.append(root)
    q.append(None)
    depth = 0
    sim = 0
    while len(q) != 0:
        t = q[0]
        q = q[1:]
        if t == None:
            depth += 1
            if len(q) == 0:
                return 'k is greater than depth'
            if depth == k:
                # return the sum of data of nodes in
                # the queue right now
                for x in q:
                    sim += x.data
                return sim
            q.append(t)
            continue

        if t.left != None:
            q.append(t.left)
        if t.right != None:
            q.append(t.right)
    return 'why this '  # never reaches this


def level_reverse_order(root):
    if root == None:
        return
    q = []
    st = []
    q.append(root)
    # q.append(None)
    while len(q) != 0:
        t = q.pop(0)
        if t.right != None:
            q.append(t.right)
        if t.left != None:
            q.append(t.left)

        st.append(t)

    while len(st) != 0:
        print(st.pop().data, end=' ')
    return
    # took this approach from the book itself,
    # to have a more advanced form of reversed
    # which gives, 4567 23 1 we have to use the
    # None technology...


def p20_path_from_root_to_leaf(root, path):
    if root == None:
        return
    path.append(root.data)
    if root.left == None and root.right == None:
        # then leaf
        print(*path)
    if root.left != None:
        p20_path_from_root_to_leaf(root.left, path)
        path.pop()
    if root.right != None:
        p20_path_from_root_to_leaf(root.right, path)
        path.pop()
    return


def p21_existence_to_path_with_given_sum(root, sum):
    if root==None:
        return
    sum -= root.data
    if sum == 0:
        print( True, root.data)
        return
    if root.left != None:
        p21_existence_to_path_with_given_sum(root.left, sum)

    if root.right != None:
        p21_existence_to_path_with_given_sum(root.right, sum)

    sum-=root.data
    return


def p24_mirror_a_given_tree(root):
    if root==None:
        return
    root.left,root.right=root.right,root.left
    if root.left!=None:
        p24_mirror_a_given_tree(root.left)
    if root.right != None:
        p24_mirror_a_given_tree(root.right)



root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
level_reverse_order(root)
#inorder(root)

#p24_mirror_a_given_tree(root)
#print()
#inorder(root)