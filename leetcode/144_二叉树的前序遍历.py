# 144. 二叉树的前序遍历 python3
#
# 给定一个二叉树，返回它的 前序 遍历。
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
# 输出: [1,2,3]
#
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？
#
# 前序遍历 根-左-右
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 递归
# 96.9%
# 执行用时：32 ms
# 内存消耗：13.8 MB
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ret = []
        def pT(node):
            ret.append(node.val)
            if node.left:
                pT(node.left)
            if node.right:
                pT(node.right)
        if root:
            pT(root)
        return ret


# 迭代
# 88%
# 执行用时：36 ms
# 内存消耗：13.6 MB
class Solution2:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        ret = []
        stack = []
        cur = root
        while stack or cur:
            while cur:
                stack.append(cur)
                ret.append(cur.val)
                cur = cur.left
            cur = stack.pop()
            cur = cur.right
        return ret


t2 = TreeNode(2)
t2.left = TreeNode(3)
t = TreeNode(1)
t.right = t2

s = Solution()
ret = s.preorderTraversal(t)
print(ret)