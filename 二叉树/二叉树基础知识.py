"""此文件是二叉树基础知识：
1.建立链式存储方式的二叉树 2.二叉树的深度和广度（层次）遍历 3.求二叉树的深度4.完全二叉树和满二叉树
5.顺序二叉树
"""
class Node(object):
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

tree = Node(1, Node(3, Node(7, Node(0)), Node(6)), Node(2, Node(5), Node(4)))
# node1 = TreeNode("A",
#                  TreeNode("B",
#                           TreeNode("D"),
#                           TreeNode("E")
#                           ),
#                  TreeNode("C",
#                           TreeNode("F"),
#                           TreeNode("G")
#                           )
#                  )
"""
二叉树的层次遍历
注意：二叉树的层次遍历即从上往下、从左至右依次打印树的节点。
其思路就是将二叉树的节点加入队列，出队的同时将其非空左右孩子依次入队，出队到队列为空即完成遍历。
"""
def levelorder(root):
    q = []
    q.append(root)
    while q:
        # 出的是节点 r，打印的是节点的值 r.data
        r = q.pop(0)
        print(r.data)
        if r.left:
            q.append(r.left)
        if r.right:
            q.append(r.right)
levelorder(tree)

######如果不输出的话，需要返回一个List的话#####
def levelorder1(root):
    q = []
    out_list = []
    q.append(root)
    while q:
        # 注意这里出的是整个节点
        r = q.pop(0)
        out_list.append(r.data)
        if r.left:
            q.append(r.left)
        if r.right:
            q.append(r.right)
        #     这里只进入结点的值就可以
    return out_list
        # print(r.data)
result = levelorder1(tree)
print(result)
"""
二叉树前序遍历（非递归）根左右，且都要进栈
自己写的：不够简洁，while循环也有点乱
"""
# def preorder(root):
#     stack = []
#     out_list = []
#     stack.append(root)
#     while stack:
#         r = stack.pop(-1)
#         out_list.append(r.data)
#         while r.left:
#             stack.append(r.left)
#             stack.pop(-1)
#             out_list.append(r.left.data)
#             if r.right:
#                 stack.append(r.right)
#             r = r.left
#     return out_list
# result = preorder(tree)
# print(result)
"""
二叉树前序遍历（非递归）根左右，且都要进栈
官方写的：
"""
def preorder(root):
    out_list = []
    stack = []
    stack.append(root)
    while stack:
        r = stack.pop(-1)
        out_list.append(r.data)
        if r.right:
            stack.append(r.right)
        if r.left:
            stack.append(r.left)
    return out_list
"""
二叉树前序遍历（递归）根左右
"""
def preorder(root):
    if root:
        print(root.data)
        preorder(root.left)
        preorder(root.right)
"""
二叉树中序遍历（非递归）根左右
"""
def inorder(root):
    stack = []
    out_list = []
    r = root
    while r or stack:
        # 改成If也可以哦
        while r:
            stack.append(r)
            r = r.left
        if stack:
            a = stack.pop(-1)
            out_list.append(a.data)
            r = a.right
    return out_list

result = inorder(tree)
print(result)
"""后序打印二叉树（非递归）
# 使用两个栈结构
# 第一个栈进栈顺序：左节点->右节点->跟节点
# 第一个栈弹出顺序： 跟节点->右节点->左节点(先序遍历栈弹出顺序：跟->左->右)
# 第二个栈存储为第一个栈的每个弹出依次进栈
# 最后第二个栈依次出栈"""
def postOrderTraverse(node):
    stack = [node]
    stack2 = []
    while len(stack) > 0:
        node = stack.pop()
        stack2.append(node)
        if node.left is not None:
            stack.append(node.left)
        if node.right is not None:
            stack.append(node.right)
    while len(stack2) > 0:
        print(stack2.pop().val)
"""
4.满二叉树和完全二叉树的概念：
满二叉树：一个二叉树，如果每一层的结点数都达到最大值，那么这个二叉树就是满二叉树。
完全二叉树：叶节点只能出现在最下层和次下层，并且最下面一层的结点都集中再该层最左边的若干位置的二叉树。
最后一个非终端节点即最后一个有子女的节点，下标从0开始，设完全二叉树最后一个叶子节点下标为n-1，则其父节点下标为(n-1-1)/2，即(n-2)/2，
则最后一个非终端的下标为(n-2)//2(用双斜杠的原因是即先做除法(/),然后向下取整(floor)，因为如果要是右叶子结点的情况的话，只用一个除法是整除
不了的，因此要用向下取整的做法)。
5.二叉树的顺序存储方式：使用列表来存储一颗二叉树
父节点和左孩子结点的下标的关系：i（父亲结点）->2i+1（左孩子结点）
父节点和右孩子结点的下标的关系：i（父亲结点）->2i+2（左孩子结点）
孩子结点和父节点的关系：i（孩子节点）->i-1/2
"""





