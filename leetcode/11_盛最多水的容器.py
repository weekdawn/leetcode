# 11.盛最多水的容器
# 难度 中等
#
# 给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点(i,ai) 。在坐标内画 n 条垂直线，
# 垂直线 i的两个端点分别为(i,ai) 和 (i, 0)。找出其中的两条线，使得它们与x轴共同构成的容器可以容纳最多的水。
#
# 说明：你不能倾斜容器，且n的值至少为 2。
#
# 图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
#
#
# 示例：
#
# 输入：[1,8,6,2,5,4,8,3,7]
# 输出：49

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j, res = 0, len(height) - 1, 0
        while i<j:
            if height[i] < height[j]:
                res = max(res, height[i] * (j - i))
                i += 1
            else:
                res = max(res, height[j] * (j-i))
                j -= 1
        return res


if __name__ == "__main__":
    s = Solution()
    ret = s.maxArea([1,8,6,2,5,4,8,3,7])
    print(ret)
