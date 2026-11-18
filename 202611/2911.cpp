class Solution {
  int dp[201][201];
  int c[201][201];

public:
  int minimumChanges(string s, int k) {
    int n = s.size();
    for (int i = 0; i < n; ++i) {
      c[i][i] = 0;
      for (int j = i + 1; j < n; ++j) {
        int cost = j - i + 1;
        int m = cost;
        for (int d = 1; d <= m / 2; ++d) {
          if (m % d)
            continue;
          int cnt = 0;
          for (int k = 0; k < d; ++k) {
            int lo = k;
            int hi = m - d + k;
            while (lo < hi) {
              if (s[i + lo] != s[i + hi])
                ++cnt;
              lo += d;
              hi -= d;
            }
          }
          cost = min(cnt, cost);
        }
        c[i][j] = cost;
      }
    }
    for (int i = 0; i < 201; ++i) {
      for (int j = 0; j < 201; ++j) {
        dp[i][j] = n;
      }
    }
    dp[0][0] = 0;
    for (int i = 1; i <= n; ++i) {
      for (int j = 1; j <= k; ++j) {
        for (int x = 0; x <= i - 2; ++x) {
          dp[i][j] = min(dp[i][j], dp[x][j - 1] + c[x][i - 1]);
        }
      }
    }
    return dp[n][k];
  }
};
