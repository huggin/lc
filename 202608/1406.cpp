class Solution {
  const int oo = 1e9;
  vector<int> stone;
  int n;
  int dp[2][50001];

  int f(int i, int round) {
    if (i >= stone.size())
      return 0;
    if (dp[round][i] != -1)
      return dp[round][i];
    int &ans = dp[round][i];
    ans = -oo;
    int tt = 0;
    for (int j = i; j < min(i + 3, n); ++j) {
      tt += stone[j];
      ans = max(ans, tt - f(j + 1, 1 - round));
    }
    return ans;
  };

public:
  string stoneGameIII(vector<int> &stoneValue) {

    stone = stoneValue;
    n = stone.size();
    memset(dp, -1, sizeof(dp));
    int diff = f(0, 0);
    if (diff > 0)
      return "Alice";
    if (diff < 0)
      return "Bob";
    return "Tie";
  }
};
