# 1 两数之和
# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
#
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
#
# 示例:
# 给定 nums = [2, 7, 11, 15], target = 9
#
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]

from typing import List
# 暴力解
# 5%
# 执行用时：6684 ms
# 内存消耗：14.6 MB
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []


# 字典表
# 88%
# 执行用时：60 ms
# 内存消耗：15.2 MB
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct = {}
        for i in range(len(nums)):
            if target - nums[i] in dct:
                return [dct[target - nums[i]], i]
            dct[nums[i]] = i
        return []


if __name__ == "__main__":
    s = Solution()
    ret = s.twoSum([2, 7, 11, 15], 9)
    print(ret)
    ret = s.twoSum([3, 2, 4], 6)
    print(ret)
    