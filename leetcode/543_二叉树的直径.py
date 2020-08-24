# 543. 二叉树的直径 python3
#
# 示例 :
# 给定二叉树
#
#       1
#      / \
#     2   3
#    / \
#   4   5
#
# 返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。
#
# 注意：两结点之间的路径长度是以它们之间边的数目表示。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 97%
# 执行用时：48 ms
# 内存消耗：15.9 MB
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        # 实际上是求左右子树的最大深度之和
        self.maxlen = 0

        def dfs(root):
            if not root:return 0
            left_dep = dfs(root.left)
            right_dep = dfs(root.right)
            if left_dep + right_dep > self.maxlen:
                self.maxlen = right_dep + left_dep
            return max(left_dep, right_dep) + 1

        dfs(root)
        return self.maxlen


t2 = TreeNode(2)
t2.left = TreeNode(3)
t = TreeNode(1)
t.right = t2

s = Solution()
ret = s.diameterOfBinaryTree(t)
print(ret)