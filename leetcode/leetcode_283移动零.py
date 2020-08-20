# 283.移动零 python3
# 简单 数组
#
# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
#
# 示例:
#
# 输入: [0,1,0,3,12]
# 输出: [1,3,12,0,0]
# 说明:
#
# 必须在原数组上操作，不能拷贝额外的数组。
# 尽量减少操作次数。
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        max_i = len(nums) - 1
        i = 0
        while i < max_i:
            if nums[i] == 0:
                j = i
                while j < max_i:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    j += 1
                max_i -= 1
            else:
                i += 1


# 95%
# 执行用时：36 ms
# 内存消耗：14.4 MB
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        max_i = len(nums) - 1
        i = 0
        while i < max_i:
            if nums[i] == 0:
                nums.append(nums.pop(i))
                max_i -= 1
            else:
                i += 1

        print(nums)


s = Solution()
nums = [0, 1, 0, 3, 12]
s.moveZeroes(nums)
nums = [0, 0, 0, 3, 12]
s.moveZeroes(nums)