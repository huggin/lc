class Solution {
  const int MOD = int(1e9 + 7);
  long long dp[1001][1001];
  long long f(int n, int k) {
    if (n < 0)
      return 0;
    if (k == 0)
      return 1;
    if (n == k)
      return 0;
    if (dp[n][k] != -1)
      return dp[n][k];
    long long &ans = dp[n][k];
    ans = f(n - 1, k);
    for (int i = n - 1; i >= k; --i) {
      ans = (ans + f(i, k - 1)) % MOD;
    }
    return ans;
  }

public:
  int numberOfSets(int n, int k) {
    memset(dp, -1, sizeof(dp));
    return f(n, k);
  }
};
