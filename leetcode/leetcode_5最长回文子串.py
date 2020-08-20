# 5 最长回文子串
# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
#
# 示例 1：
# 输入: “babad”
# 输出: “bab”
# 注意: “aba” 也是一个有效答案。
#
# 示例 2：
# 输入: “cbbd”
# 输出: “bb”
#
# 分析过程
# 回文串 就是 正序和逆序是一个结果的字符串叫回文串
# 最长回文子串 是找出 在字符串中 正序和逆序是一个结果的子串

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2: return s

        max_len = 0
        start_index = 0

        def hw_len(left, right):
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1, left + 1

        # 中心扩散法
        for i in range(n-1):
            # 单核心
            len1, start_index1 = hw_len(i, i)
            # 双核心
            len2, start_index2 = hw_len(i, i+1)

            if len1 > max_len:
                max_len = len1
                start_index = start_index1
            if len2 > max_len:
                max_len = len2
                start_index = start_index2

        return s[start_index: start_index+max_len]


s = Solution()
st = "cbbd"
ret = s.longestPalindrome(st)
print(ret, 'bb')
st = "babad"
ret = s.longestPalindrome(st)
print(ret, 'bab')
st = "abcda"
ret = s.longestPalindrome(st)
print(ret, "a")
st = "ac"
ret = s.longestPalindrome(st)
print(ret, 'a')
st = "bb"
ret = s.longestPalindrome(st)
print(ret, 'bb')
st = ""
ret = s.longestPalindrome(st)
print(ret)
st = "aacedaa"
ret = s.longestPalindrome(st)
print(ret, "aa")
st = "aacdefcaa"
ret = s.longestPalindrome(st)
print(ret, "aa")
st = "saacdefcaa"
ret = s.longestPalindrome(st)
print(ret, "aa")
st = "abcdbbfcba"
ret = s.longestPalindrome(st)
print(ret, "bb")
st = "onoranynartionso"
ret = s.longestPalindrome(st)
print(ret, "ranynar")