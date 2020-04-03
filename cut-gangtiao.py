from typing import List


# 切钢条 [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
class Solution:
    memo = []
    max_arr = [0]
    # 递归  当 n 大了以后 贼鸡巴慢
    def cut_recursion(self, p: List[int], n) -> int:
        if n == 0:
            return 0
        m = 0
        for i in range(1, n + 1 if n < len(p) else len(p) + 1):
            m = max(m, p[i - 1] + self.cut(p, n - i))
        return m

    # 备忘录方法
    def cut_memorandum(self, p: List[int], n) -> int:
        self.cut_memorandum_init(n)
        return self.cut_memorandum_operate(p, n)

    # 备忘录 初始化 一个列表
    def cut_memorandum_init(self, n):
        for i in range(0, n):
            self.memo.append(-1)

    def cut_memorandum_operate(self, p, n):
        if n == 0:
            return 0
        elif self.memo[n - 1] != -1:
            return self.memo[n - 1]
        m = 0
        for i in range(1, n + 1 if n < len(p) else len(p) + 1):
            m = max(m, p[i - 1] + self.cut_memorandum_operate(p, n - i))
        self.memo[n - 1] = m
        return m

    # 自底向上的动态规划
    def cut_bottom_up(self, p: List[int], n) -> int:

        for i in range(1, n + 1):
            q = 0
            for j in range(1, i + 1 if i < len(p) else len(p) + 1):
                q = max(q, p[j - 1] + self.max_arr[i - j])
            self.max_arr.append(q)
        return self.max_arr[n - 1]


if __name__ == '__main__':
    solution = Solution()
    # print(Solution().cut_recursion([1, 5, 8, 9, 10, 17, 17, 20, 24, 30], 20))
    print(solution.cut_memorandum([1, 5, 8, 9, 10, 17, 17, 20, 24, 30], 100))
    print(solution.cut_bottom_up([1, 5, 8, 9, 10, 17, 17, 20, 24, 30], 100))
    print(solution.max_arr)
