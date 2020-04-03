class Solution:
    # 递归
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        if n < 0:
            return 1 / self.myPow(x, -n)
        return self.myPow(x * x, n // 2) if n % 2 == 0 else x * self.myPow(x, n - 1)

    # 位运算
    def myPow2(self, x: float, n: int) -> float:
        if n < 0:
            return 1 / self.myPow(x, -n)
        res = 1
        while n:
            if n & 1 == 1:
                res *= x
            x *= x
            n >>= 1
        return res