class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, n):
        i = 1
        if n == 0:
            return -1;
        if n == 1:
            return 1;
        while i * i <= n:
            if n % i == 0:
                if i != 1 and i == n / i:
                    return int(i)
            i += 1
        return int(-1)



soln = Solution()
print(soln.solve(int(input())))
