"""104. 二叉树的最大深度
给定一个二叉树，找出其最大深度。
二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
说明: 叶子节点是指没有子节点的节点。
"""
# Definition for a binary tree node.
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Node):
        # DFS
        if root is None:
            return 0
        stack = [(1, root)]
        depth = 0
        while stack:
            cur_dep, node = stack.pop()
            depth = max(depth, cur_dep)
            if node.right:
                stack.append((cur_dep+1,node.right))
            if node.left:
                stack.append((cur_dep+1,node.left))
        return depth
solution = Solution()
tree = Node(1, Node(3, Node(7, Node(0)), Node(6)), Node(2, Node(5), Node(4)))
result = solution.maxDepth(tree)
print(result)