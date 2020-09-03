# 12.整数转罗马数字
# 难度 中等
# 罗马数字包含以下七种字符：I，V，X，L，C，D和M。
#
# 字符          数值
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# 例如， 罗马数字 2 写做II，即为两个并列的 1。12 写做XII，即为X+II。 27 写做XXVII, 即为XX+V+II。
#
# 通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做IIII，而是IV。
# 数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为IX。
# 这个特殊的规则只适用于以下六种情况：
#
# I可以放在V(5) 和X(10) 的左边，来表示 4 和 9。
# X可以放在L(50) 和C(100) 的左边，来表示 40 和90。
# C可以放在D(500) 和M(1000) 的左边，来表示400 和900。
# 给定一个整数，将其转为罗马数字。输入确保在 1到 3999 的范围内。
#
# 示例1:
#
# 输入:3
# 输出: "III"
# 示例2:
#
# 输入:4
# 输出: "IV"
# 示例3:
#
# 输入:9
# 输出: "IX"
# 示例4:
#
# 输入:58
# 输出: "LVIII"
# 解释: L = 50, V = 5, III = 3.
# 示例5:
#
# 输入:1994
# 输出: "MCMXCIV"
# 解释: M = 1000, CM = 900, XC = 90, IV = 4.

class Solution:
    def intToRoman(self, num: int) -> str:
        digits = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"),
          (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
        roman_digits = []
        for value, symbol in digits:
            if num == 0:
                break
            count, num = divmod(num, value)
            roman_digits.append(symbol * count)
        return "".join(roman_digits)


if __name__ == "__main__":
    s = Solution()
    ret = s.intToRoman(3)
    print(ret)
    ret = s.intToRoman(1994)
    print(ret)
