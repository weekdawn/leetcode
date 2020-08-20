# 567. 字符串的排列 python3
#
# 给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。
# 
# 换句话说，第一个字符串的排列之一是第二个字符串的子串。
#
# 示例1:
# 输入: s1 = “ab” s2 = “eidbaooo”
# 输出: True
# 解释: s2 包含 s1 的排列之一 (“ba”).
#
# 示例2:
# 输入: s1= “ab” s2 = “eidboaoo”
# 输出: False
#
# 注意：
# 输入的字符串只包含小写字母
# 两个字符串的长度都在 [1, 10,000] 之间
#
# 分析：
# 相同个数的字符的子序列个数是相同的，判断自序的时候可以借助字典进行比较
# collections.Counter(s1)
# 返回字符串各字符的个数，窗口移动时计算新串的字典，但这样的时间复杂度是比较高的 方法一
#
# 我们考虑第一次时计算两个相同长度的字典，剩下的字典只对原有字典进行移动窗口的编辑，也就方法三

# 方法一
# 执行用时： 1440 ms , 在所有 Python3 提交中击败了 30.15% 的用户
# 内存消耗： 13.8 MB , 在所有 Python3 提交中击败了 7.69% 的用户
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        import collections
        count_dict = collections.Counter(s1)
        i = 0
        j = len(s1)
        m = len(s2)
        while j < m + 1:
            if collections.Counter(s2[i:j]) == count_dict:
                return True
            i += 1
            j += 1
        return False


# 方法二
# 执行用时： 4540 ms , 在所有 Python3 提交中击败了 9.83% 的用户
# 内存消耗： 13.9 MB , 在所有 Python3 提交中击败了 7.69% 的用户
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        i = 0
        j = len(s1)
        m = len(s2)
        while j < m + 1:
            if sorted(s2[i:j]) == s1:
                return True
            i += 1
            j += 1
        return False


# 方法三
# 执行用时： 80 ms , 在所有 Python3 提交中击败了 87.88% 的用户
# 内存消耗： 13.6 MB , 在所有 Python3 提交中击败了 7.69% 的用户
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        j = len(s1)
        m = len(s2)
        if j > m: return False

        dict1 = {}
        dict2 = {}
        for i in range(j):
            dict1[s1[i]] = dict1.get(s1[i], 0) + 1
            dict2[s2[i]] = dict2.get(s2[i], 0) + 1
        if dict1 == dict2:
            return True

        i = 0
        while j < m:
            # 想法与第一种一样，需要等记每个字符的个数
            # 但是窗口移动时只变化字典中移动的字符，减少计算次数
            dict2[s2[j]] = dict2.get(s2[j], 0) + 1
            dict2[s2[i]] = dict2.get(s2[i], 0) - 1
            if dict2.get(s2[i]) == 0:
                dict2.pop(s2[i])

            if dict2 == dict1:
                return True
            i += 1
            j += 1
        return False


# 方法四
# 执行用时： 76 ms , 在所有 Python3 提交中击败了 91.79% 的用户
# 内存消耗： 13.9 MB , 在所有 Python3 提交中击败了 7.69% 的用户
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        j = len(s1)
        m = len(s2)
        if j > m: return False

        import collections

        dict1 = collections.Counter(s1)
        dict2 = collections.Counter(s2[0:j])
        if dict1 == dict2:
            return True

        i = 0
        while j < m:
            # 想法与第一种一样，需要等记每个字符的个数
            # 但是窗口移动时只变化字典中移动的字符，减少计算次数
            dict2[s2[j]] = dict2.get(s2[j], 0) + 1
            dict2[s2[i]] = dict2.get(s2[i], 0) - 1
            if dict2.get(s2[i]) == 0:
                dict2.pop(s2[i])

            if dict2 == dict1:
                return True
            i += 1
            j += 1
        return False


s = Solution()
s1 = "ab"
s2 = "eidbaooo"
ret = s.checkInclusion(s1, s2)
print(ret, ret == True)
s1 = "ab"
s2 = "eidboaoo"
ret = s.checkInclusion(s1, s2)
print(ret, ret == False)
s1 = "adc"
s2 = "dcda"
ret = s.checkInclusion(s1, s2)
print(ret, ret == True)