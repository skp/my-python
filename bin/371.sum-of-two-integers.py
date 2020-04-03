class Solution:
    def getSum(self, a: int, b: int) -> int:
        if a == 0:
            return b
        if b == 0:
            return a
        print(bin(a).replace('0b', '').zfill(8))
        print(bin(b).replace('0b', '').zfill(8))
        print(bin(a ^ b).replace('0b', '').zfill(8))
        print(bin(a & b).replace('0b', '').zfill(8), '\n')
        return self.getSum(a ^ b, (a & b) << 1)


if __name__ == '__main__':
    print(Solution().getSum(34, 51))
