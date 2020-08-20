# 88. 合并两个有序数组 python3
#
# 给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。
#
# 说明:
#
# 初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
# 你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
#
# 示例:
# 输入:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6], n = 3
#
# 输出: [1,2,2,3,5,6]

from typing import List
# 73%
# 执行用时：40 ms
# 内存消耗：13.6 MB
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        while j >= 0:
            if nums1[i] < nums2[j]:
                nums1[i + j + 1] = nums2[j]
                j -= 1
            else:
                if i == -1:
                    nums1[j] = nums2[j]
                    j -= 1
                else:
                    nums1[i + j + 1] = nums1[i]
                    i -= 1


s = Solution()

nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]
m = 3
n = 3
s.merge(nums1, m, nums2, n)
print(nums1)
nums1 = [2, 5, 6, 0, 0, 0]
nums2 = [1, 2, 3]
m = 3
n = 3
s.merge(nums1, m, nums2, n)
print(nums1)