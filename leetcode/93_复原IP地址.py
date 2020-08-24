# 93. 复原IP地址 python3
# 中等 字节
#
# 给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。
#
# 有效的 IP 地址正好由四个整数（每个整数位于 0 到 255 之间组成），整数之间用 ‘.’ 分隔。
#
# 示例:
#
# 输入: “25525511135”
# 输出: [“255.255.11.135”, “255.255.111.35”]
from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 12 or len(s) < 4:
            return []

        def is_valid(num):
            if not num or int(num) > 255 or (len(num) > 1 and num[0] == '0'):
                return False
            return True

        res = []
        str_length = len(s)
        for i in range(str_length):
            if not is_valid(s[:i]):continue
            for j in range(i,str_length):
                if not is_valid(s[i:j]):continue
                for k in range(j,str_length):
                    if not is_valid(s[j:k]):continue
                    if not is_valid(s[k:]):continue
                    res.append(s[:i]+'.'+s[i:j]+'.'+s[j:k]+'.'+s[k:])

        return res

s = Solution()
nums = "25525511135"
ret = s.restoreIpAddresses(nums)
print(ret)

nums = "2552551113"
ret = s.restoreIpAddresses(nums)
print(ret)

nums = "255251135"
ret = s.restoreIpAddresses(nums)
print(ret)

nums = "2552"
ret = s.restoreIpAddresses(nums)
print(ret)

nums = "2"
ret = s.restoreIpAddresses(nums)
print(ret)

nums = "010010"
ret = s.restoreIpAddresses(nums)
print(ret, ret == ["0.10.0.10", "0.100.1.0"])
