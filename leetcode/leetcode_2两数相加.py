# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 61%
# 执行用时：76 ms
# 内存消耗：13.7 MB
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ret = ls = ListNode(0)
        while l1 or l2:
            if l1:
                ls.val += l1.val
                l1 = l1.next
            if l2:
                ls.val += l2.val
                l2 = l2.next

            if ls.val > 9:
                ls.val = ls.val - 10
                ls.next = ListNode(1)
                ls = ls.next
            else:
                if l1 or l2:
                    ls.next = ListNode(0)
                    ls = ls.next
        return ret


s1 = ListNode(2)
s1.next = ListNode(4)
s1.next.next = ListNode(3)

s2 = ListNode(5)
s2.next = ListNode(6)
s2.next.next = ListNode(6)
s2.next.next.next = ListNode(6)
s2.next.next.next.next = ListNode(6)

s = Solution()
ret = s.addTwoNumbers(s1, s2)
while ret:
    print(ret.val)
    ret = ret.next