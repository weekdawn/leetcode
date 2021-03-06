# 468. 验证IP地址 python3
# 中等 字符串
#
# 编写一个函数来验证输入的字符串是否是有效的 IPv4 或 IPv6 地址。
# IPv4 地址由十进制数和点来表示，每个地址包含4个十进制数，其范围为 0 - 255， 用(".")分割。比如，172.16.254.1；
# 同时，IPv4 地址内的数不会以 0 开头。比如，地址 172.16.254.01 是不合法的。
# IPv6 地址由8组16进制的数字来表示，每组表示 16 比特。这些组数字通过 (":")分割。
# 比如, 2001:0db8:85a3:0000:0000:8a2e:0370:7334 是一个有效的地址。
# 而且，我们可以加入一些以 0 开头的数字，字母可以使用大写，也可以是小写。
# 所以， 2001:db8:85a3:0:0:8A2E:0370:7334 也是一个有效的 IPv6 address地址 (即，忽略 0 开头，忽略大小写)。
# 然而，我们不能因为某个组的值为 0，而使用一个空的组，以至于出现 (::)😃😃😃 的情况。
# 比如， 2001:0db8:85a3::8A2E:0370:7334 是无效的 IPv6 地址。
# 同时，在 IPv6 地址中，多余的 0 也是不被允许的。比如， 02001:0db8:85a3:0000:0000:8a2e:0370:7334 是无效的。
# 说明: 你可以认为给定的字符串里没有空格或者其他特殊字符。
# 示例 1:
# 输入: “172.16.254.1”
#
# 输出: “IPv4”
#
# 解释: 这是一个有效的 IPv4 地址, 所以返回 “IPv4”。
#
# 示例 2:
# 输入: “2001:0db8:85a3:0:0:8A2E:0370:7334”
#
# 输出: “IPv6”
#
# 解释: 这是一个有效的 IPv6 地址, 所以返回 “IPv6”。
#
# 示例 3:
# 输入: “256.256.256.256”
#
# 输出: “Neither”
#
# 解释:
# 这个地址既不是 IPv4 也不是 IPv6 地址。


# 执行用时：44 ms , 在所有 Python3 提交中击败了 41.10% 的用户
# 内存消耗：13.4 MB, 在所有 Python3 提交中击败了 100.00% 的用户
class Solution:
    def validIPAddress(self, IP: str) -> str:

        def is_IPv4():
            for i in IP.split('.'):
                if len(i) < 1 or i > "255" or (i[0] == "0" and i != "0"):
                    return "Neither"
            return "IPv4"

        def is_IPv6():
            for x in IP.split(':'):
                if 0 < len(x) <= 4:
                    for i in x:
                        if not ("a" <= i <= "f" or "A" <= i <= "F" or "0" <= i <= "9"):
                            return "Neither"
                else:
                    return "Neither"

            return "IPv6"

        if 7 <= len(IP) <= 39:
            if IP.count('.') == 3:
                return is_IPv4()
            elif IP.count(':') == 7:
                return is_IPv6()
        return "Neither"


s = Solution()
ip = "172.16.254.1"
ret = s.validIPAddress(ip)
print(ret, ret == "IPv4")
ip = "102.16.254.0"
ret = s.validIPAddress(ip)
print(ret, ret == "IPv4")
ip = "102.016.254.0"
ret = s.validIPAddress(ip)
print(ret, ret == "Neither")
ip = "256.256.256.256"
ret = s.validIPAddress(ip)
print(ret, ret == "Neither")
ip = "1e1.4.5.6"
ret = s.validIPAddress(ip)
print(ret, ret == "Neither")
ip = "00.0.0.0"
ret = s.validIPAddress(ip)
print(ret, ret == "Neither")
ip = "2001:0db8:85a3:0:0:8A2E:0370:7334"
ret = s.validIPAddress(ip)
print(ret, ret == "IPv6")
ip = "02001:0db8:85a3:0:0:8A2E:0370:7334"
ret = s.validIPAddress(ip)
print(ret, ret == "Neither")
ip = "2001:0db8:85a3:0:0:8A2E:0370:7334:"
ret = s.validIPAddress(ip)
print(ret, ret == "Neither")