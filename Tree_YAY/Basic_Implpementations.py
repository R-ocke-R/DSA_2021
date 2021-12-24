class TreeNode:
    def __init__(self,value):
        self.data = value
        self.left =None
        self.right=None

def inorder(root):
    if root==None:
        return
    # Inorder means -> left then root then right
    inorder(root.left)
    print(root.data, end= '->')
    inorder(root.right)
    return

def preorder(root):
    if root==None:
        return
    # Inorder means -> root then left then right
    print(root.data)
    preorder(root.left)
    preorder(root.right)
    return

def postorder(root):
    if root==None:
        return
    # Inorder means -> left then right then root.
    postorder(root.left)
    postorder(root.right)
    print(root.data)
    return

def FindMax(root):
    if root==None:
        return
    global maxx
    maxx=max(maxx, root.data)
    FindMax(root.left)
    FindMax(root.right)
    return

def find_max_recursion(root):
    # this concept uses level order, which I aint
    # aware of rn.
    size=0
    maxx=0
    st=[]
    st.append(root)
    while len(st)!=0:
        ele=st.pop(0)
        size+=1
        #print(ele.data)
        maxx=max(maxx, ele.data)
        if ele.left:
            st.append(ele.left)
        if ele.right:
            st.append(ele.right)
    print(maxx)
    print("size of nodes of tree", size)

def searching(item, root):
    global found
    if root==None or found==True:
        return
    if root.data == item:
        found=True
        return
    searching(item, root.left)
    searching(item, root.right)
    return


'''
       1
   2      5 
 3   4       6 

'''

root=TreeNode(1)
root.left=TreeNode(2)
root.left.left=TreeNode(3)
root.left.right=TreeNode(4)
root.right=TreeNode(5)
root.right.right=TreeNode(6)

maxx = root.data        #for finding max function


found=False
#searching(7, root)
print(found)
find_max_recursion(root)
