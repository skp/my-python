class Solution:
    m = 0

    def move(self, disks, a, c):
        self.m += 1
        print("第", self.m, " 次移动 : ", " 把 ", disks, " 号圆盘从 ", a, " ->移到->  ", c)

    def hanoi(self, n, a, b, c):
        if n == 1:
            self.move(n, a, c)
        else:
            self.hanoi((n - 1), a, c, b)
            self.move(n, a, c)
            self.hanoi((n - 1), b, a, c)


if __name__ == '__main__':
    print(Solution().hanoi(5, 'a', 'b', 'c'))