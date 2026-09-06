class Solution {
public:
  int numDistinct(string s, string t) {
    int m = s.size();
    int n = t.size();
    vector<vector<int>> dp(m, vector<int>(n, -1));
    function<int(int, int)> f = [&](int i, int j) {
      if (j == n)
        return 1;
      if (i == m)
        return 0;
      if (dp[i][j] != -1)
        return dp[i][j];
      int &ans = dp[i][j];
      ans = f(i + 1, j);
      if (s[i] == t[j]) {
        ans += f(i + 1, j + 1);
      }

      return ans;
    };
    return f(0, 0);
  }
};
