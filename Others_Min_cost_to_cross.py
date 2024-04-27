def minCostToCrossRiver(platforms, k):
    n = len(platforms)
    dp = [float('inf')] * (n+1)
    dp[0] = 0  # Cost to reach the first platform is 0
    for i in range(1, n+1):
        for j in range(0, min(k, i) + 1):  # Check the last k platforms
            dp[i] = min(dp[i], platforms[i-1] + dp[i-j])
    answer = float('inf')
    for i in range(k):
        answer = min(answer, dp[n-i])
    return answer

# Example usage
platforms = [4, 7, 2, 11, 3, 5, 8, 6, 10]
k = 4
print("Minimum cost to cross the river:", minCostToCrossRiver(platforms, k))
