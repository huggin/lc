class Solution {
  string s;
  int dp[101][101];
  int f(int k, int cnt) {
    if (cnt < 0)
      return 0;
    if (k == s.size()) {
      if (cnt == 0)
        return 1;
      else
        return 0;
    }
    if (dp[k][cnt] != -1)
      return dp[k][cnt];
    int &ans = dp[k][cnt];
    if (s[k] == '(') {
      return ans = f(k + 1, cnt + 1);
    } else if (s[k] == ')') {
      return ans = f(k + 1, cnt - 1);
    } else {
      return ans = f(k + 1, cnt) || f(k + 1, cnt + 1) || f(k + 1, cnt - 1);
    }
  }

public:
  bool checkValidString(string s) {
    this->s = s;
    memset(dp, -1, sizeof(dp));
    return f(0, 0);
  }
};
