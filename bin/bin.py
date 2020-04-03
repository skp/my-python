class Solution:
    def printBinary(self, i: int) -> str:
        return bin(i).replace('0b', '').zfill(32)


if __name__ == '__main__':
    print(Solution().printBinary(10))
    print(Solution().printBinary(3))