# 145. 二叉树的后序遍历 python3
#
# 给定一个二叉树，返回它的 后序 遍历。
#
# 示例:
# 输入: [1,null,2,3]
#
#    1
#     \
#      2
#     /
#    3
# 1
# 2
# 3
# 4
# 5
# 输出: [3,2,1]
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 递归
# 44%
# 执行用时：44 ms
# 内存消耗：13.8 MB
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ret = []
        def pT(node):
            if node.left:
                pT(node.left)
            if node.right:
                pT(node.right)
            ret.append(node.val)
        if root:
            pT(root)
        return ret


# 88%
# 执行用时：36 ms
# 内存消耗：13.7 MB
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        stack = [root]
        ret = []

        while stack:
            node = stack.pop()
            ret.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        ret.reverse()
        return ret


t2 = TreeNode(2)
t2.left = TreeNode(3)
t = TreeNode(1)
t.right = t2

s = Solution()
ret = s.preorderTraversal(t)
print(ret)