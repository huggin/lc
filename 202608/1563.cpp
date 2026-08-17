class Solution {
  vector<int> ps;
  int dp[501][501];
  int f(int i, int j) {
    if (i + 1 > j)
      return 0;
    if (dp[i][j] != -1)
      return dp[i][j];
    int &ans = dp[i][j];
    ans = 0;
    for (int k = i; k < j; ++k) {
      int left = ps[k + 1] - ps[i];
      int right = ps[j + 1] - ps[k + 1];
      if (left == right) {
        ans = max(ans, left + max(f(k + 1, j), f(i, k)));
      } else if (left < right) {
        ans = max(ans, left + f(i, k));
      } else {
        ans = max(ans, right + f(k + 1, j));
      }
    }
    return ans;
  };

public:
  int stoneGameV(vector<int> &stoneValue) {
    int n = stoneValue.size();
    ps.resize(n + 1);
    for (int i = 0; i < n; ++i) {
      ps[i + 1] = ps[i] + stoneValue[i];
    }
    memset(dp, -1, sizeof(dp));
    return f(0, n - 1);
  }
};
