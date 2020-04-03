from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """回溯法"""

        res = []

        def helper(s, tmp):
            """
            如果是空字符串，说明已经处理完毕
            否则逐个字符往前测试，判断是否是回文
            如果是，则处理剩余字符串，并将已经得到的列表作为参数
            """
            if not s:
                res.append(tmp)
            for i in range(1, len(s) + 1):
                if s[:i] == s[:i][::-1]:
                    helper(s[i:], tmp + [s[:i]])

        helper(s, [])
        return res


if __name__ == '__main__':
    print(Solution().partition('sbdbdbdsd'))
