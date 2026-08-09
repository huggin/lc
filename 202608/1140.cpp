class Solution {
  int dp[101][101][2];
  vector<int> p;
  const int oo = 1'000'000'007;
  int f(int i, int m, int alice) {
    if (i >= p.size())
      return 0;
    if (dp[i][m][alice] != -1)
      return dp[i][m][alice];
    int &ans = dp[i][m][alice];
    ans = -oo;
    int curr = 0;
    for (int j = 0; j < 2 * m && i + j < p.size(); ++j) {
      curr += p[i + j];
      ans = max(ans, curr - f(i + j + 1, max(m, j + 1), 1 - alice));
    }
    return ans;
  }

public:
  int stoneGameII(vector<int> &piles) {
    p = piles;
    memset(dp, -1, sizeof(dp));
    int diff = f(0, 1, 0);
    int total = reduce(begin(piles), end(piles), 0);
    return (total + diff) / 2;
  }
};
