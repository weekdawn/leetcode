# 153. 寻找旋转排序数组中的最小值 python3
# 中等 二分查找
#
# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
#
# ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
#
# 请找出其中最小的元素。
#
# 你可以假设数组中不存在重复元素。
#
# 示例 1:
# 输入: [3,4,5,1,2]
# 输出: 1
#
# 示例 2:
# 输入: [4,5,6,7,0,1,2]
# 输出: 0

from typing import List

# 89%
# 执行用时：36 ms
# 内存消耗：13.8 MB
class Solution:
    def findMin(self, nums: List[int]) -> int:

        n = len(nums)
        left = 0
        rigth = n - 1
        while left+1 < rigth:
            i = (left+rigth) // 2
            if nums[i] < nums[rigth]:
                rigth = i
            elif nums[left] < nums[i]:
                left = i

        return nums[left] if nums[left] < nums[rigth] else nums[rigth]


s = Solution()
nums = [3, 4, 5, 1, 2]
ret = s.findMin(nums)
print(ret, ret == 1)
nums = [4, 5, 6, 7, 0, 1, 2]
ret = s.findMin(nums)
print(ret, ret == 0)
nums = [1, 4]
ret = s.findMin(nums)
print(ret, ret == 1)
nums = [1, 2, 3]
ret = s.findMin(nums)
print(ret, ret == 1)
nums = [1]
ret = s.findMin(nums)
print(ret, ret == 1)
nums = [3, 4, 5, 1, 2]
ret = s.findMin(nums)
print(ret, ret == 1)