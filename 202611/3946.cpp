class Solution {
  int dp[1001][2][1501];

public:
  int maximumSaleItems(vector<vector<int>> &items, int budget) {
    int n = items.size();
    vector<int> bonus(n);
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < n; ++j) {
        if (j == i)
          continue;
        if (items[i][0] % items[j][0] == 0) {
          ++bonus[j];
        }
      }
    }
    memset(dp, -1, sizeof(dp));
    function<int(int, int, int)> f = [&](int i, int bought, int b) {
      if (i == n)
        return 0;
      if (dp[i][bought][b] != -1)
        return dp[i][bought][b];
      int &ans = dp[i][bought][b];
      ans = f(i + 1, 0, b);
      if (items[i][1] <= b) {
        if (bought == 0) {
          ans = max(ans, 1 + bonus[i] + f(i, 1, b - items[i][1]));
        } else {
          ans = max(ans, 1 + f(i, 1, b - items[i][1]));
        }
      }
      return ans;
    };
    return f(0, 0, budget);
  }
};
