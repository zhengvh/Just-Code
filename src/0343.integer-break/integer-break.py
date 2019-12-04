class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0]*(n+1)
        for i in range(2,n+1):
            for j in range(1,i):
                dp[i] = max(dp[i], max(dp[j]*(i-j), j*(i-j)))
        return dp[n]