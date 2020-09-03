# 141.环形链表
# 给定一个链表，判断链表中是否有环。
#
# 为了表示给定链表中的环，我们使用整数pos来表示链表尾连接到链表中的位置（索引从0开始）。 如果
# pos是 - 1，则在该链表中没有环。
#
#
#
# 示例
# 1：
#
# 输入：head = [3, 2, 0, -4], pos = 1
# 输出：true
# 解释：链表中有一个环，其尾部连接到第二个节点。
#
#
# 示例
# 2：
#
# 输入：head = [1, 2], pos = 0
# 输出：true
# 解释：链表中有一个环，其尾部连接到第一个节点。
#
#
# 示例
# 3：
#
# 输入：head = [1], pos = -1
# 输出：false
# 解释：链表中没有环。
# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 字典实现哈希表
class Solution1:
    def hasCycle(self, head: ListNode) -> bool:
        dic = {}
        node = head
        while node:
            if dic.get(node,0)!=0:#如果不存在get返回的是0
                return True
            else:#不存在
                dic[node] = 1
            node = node.next
        return False

# 借助辅助空间
class Solutio2:
    def hasCycle(self, head: ListNode) -> bool:
        a = set()
        while head:

            if head in a:
                return True

            a.add(head)
            head = head.next
        return False

# 快慢指针法
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = fast = head
        # if not head：  # 没必要这样写可以加入while循环判断更简洁
        #     return False

        while fast and fast.next:  # 防止head为空和出现空指针的next的情况
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True

        return False

s = Solution()
t1 = ListNode(3)
t1.next = ListNode(2)
t1.next.next = ListNode(0)
t1.next.next.next = ListNode(4)
print(s.hasCycle(t1))
