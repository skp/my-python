from typing import List

# 动态规划的两个方向
class Solution:

    # 自顶向下的备忘录法 创建一个数组来保存先前计算过的值
    # 缺点是递归 产生的额外开销
    def fibonacci_beiwanglu(self, n) -> int:
        if n <= 0:
            return n
        memo = []
        for i in range(0, n + 1):
            memo.append(-1)

        return self.fib(n, memo)

    def fib(self, n, memo):
        if memo[n] != -1:
            return memo[n]
        # 如果已经求出了fib（n）的值直接返回，否则将求出的值保存在memo备忘录中。
        if n <= 2:
            memo[n] = 1
        else:
            memo[n] = self.fib(n - 1, memo) + self.fib(n - 2, memo)
        return memo[n]

    # 自底向上的动态规划 空间1
    def fibonacci_zidixiangshang(self, n) -> int:
        if n < 1:
            return 0
        memo_1 = 1
        memo_2 = 1
        for i in range(2, n + 1):
            memo_3 = memo_1 + memo_2
            memo_1 = memo_2
            memo_2 = memo_3
        return memo_3


if __name__ == '__main__':
    print(Solution().fibonacci_zidixiangshang(5))
