class Solution {
public:
  int longestValidParentheses(string s) {
    stack<int> si;
    int ans = 0;
    int n = s.size();
    vector<int> pair(n, -1);
    for (auto [i, c] : views::enumerate(s)) {
      if (c == '(') {
        si.push(i);
      } else if (!si.empty()) {
        pair[i] = si.top();
        si.pop();
      }
    }
    int i = n - 1;
    int cnt = 0;
    while (i >= 0) {
      if (s[i] == '(' || pair[i] == -1) {
        --i;
        cnt = 0;
      } else {
        cnt += i - pair[i] + 1;
        i = pair[i] - 1;
      }
      ans = max(ans, cnt);
    }
    return ans;
  }
};
