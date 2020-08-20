# 151 翻转字符串里的单词 python3
#
# 给定一个字符串，逐个翻转字符串中的每个单词。
#
# 示例 1：
# 输入: “the sky is blue”
# 输出: “blue is sky the”
#
# 示例 2：
# 输入: " hello world! "
# 输出: “world! hello”
# 解释: 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
#
# 示例 3：
# 输入: “a good example”
# 输出: “example good a”
#
# 解释:
# 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
#
# 说明：
# 无空格字符构成一个单词。
# 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
# 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
#
# 进阶：
#
# 请选用 C 语言的用户尝试使用 O(1) 额外空间复杂度的原地解法。

# 91%
# 执行用时：36 ms
# 内存消耗：13.9 MB
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[:: -1])


# 58%
# 执行用时：44 ms
# 内存消耗：13.8 MB
class Solution2:
    def reverseWords(self, s: str) -> str:
        if not s: return s
        ret = s.split()
        i = 0
        j = len(ret) - 1
        while i < j:
            ret[i], ret[j] = ret[j], ret[i]
            i += 1
            j -= 1

        return " ".join(ret)


if __name__ == "__main__":
    s = Solution()
    sp = "the sky is blue"
    ret = s.reverseWords(sp)
    print(ret)
    sp = "a good  example"
    ret = s.reverseWords(sp)
    print(ret)
    sp = " hello world! "
    ret = s.reverseWords(sp)
    print(ret)