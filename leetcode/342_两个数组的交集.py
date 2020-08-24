# 349. 两个数组的交集 python3
#
# 给定两个数组，编写一个函数来计算它们的交集。
#
# 示例 1：
# 输入：nums1 = [1,2,2,1], nums2 = [2,2]
# 输出：[2]
#
# 示例 2：
# 输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# 输出：[9,4]
#
# 说明：
#
# 输出结果中的每个元素一定是唯一的。
# 我们可以不考虑输出结果的顺序。
from typing import List

# 93.58%
# 执行用时：52 ms
# 内存消耗：13.7 MB
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set1.intersection(set2))


s = Solution()
nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]

ret = s.intersection(nums1, nums2)
print(ret)