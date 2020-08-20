# 15. 三数之和 python3
#
# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。
#
# 注意：答案中不可以包含重复的三元组。
#
# 示例：
# 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
#
# 满足要求的三元组集合为：
# [
# [-1, 0, 1],
# [-1, -1, 2]
# ]
from typing import List

# 44.8%
# 执行用时：1040 ms
# 内存消耗：16.2 MB
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = []
        nl = len(nums)
        if nl < 3:
            return ret
        nums.sort()
        for i in range(nl):
            # 最左侧数大于0 没有结果了
            if nums[i] > 0:
                break
            # 过滤 重复结果
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = nl - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    ret.append([nums[i], nums[l], nums[r]])
                    # 过滤 重复结果
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    # 过滤 重复结果
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    l += 1
        return ret


import bisect

k
class Solution2:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = []
        nl = len(nums)
        if nl < 3:
            return ret

        counts = {}
        for n in nums:
            counts[n] = counts.get(n, 0) + 1   # 统计每个数出现的次数

        nums = sorted(counts)

        for i in range(len(nums)):
            if counts[nums[i]] > 1:
                if nums[i] == 0 and counts[nums[i]] > 2:
                    ret.append([0, 0, 0])
                else:
                    if 0 - (nums[i] * 2) in counts:
                        ret.append([nums[i], nums[i], -nums[i] * 2])

            if nums[i] < 0:
                rmax_num = (0 - nums[i])
                for num in nums[i: bisect.bisect_right(nums, rmax_num//2)]:
                    x = rmax_num - num
                    if x in counts and x != num:
                        ret.append([num, x, rmax_num])
        return ret


if __name__ == "__main__":
    s = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    ret = s.threeSum(nums)
    print(ret)
    nums = [0, 0, 0]
    ret = s.threeSum(nums)
    print(ret)
    nums = [0, 0, 0, 0]
    ret = s.threeSum(nums)
    print(ret)
    nums = [-1, 0, 1]
    ret = s.threeSum(nums)
    print(ret)
    nums = [3, 0, -2, -1, 1, 2]
    ret = s.threeSum(nums)
    print(ret)