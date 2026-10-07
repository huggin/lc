class Solution {
public:
  vector<string> removeInvalidParentheses(string s) {
    int cnt = 0;
    int pair = 0;
    int alpha = 0;
    for (char c : s) {
      if (c == '(') {
        ++cnt;
      } else if (c == ')') {
        if (cnt > 0) {
          --cnt;
          ++pair;
        }
      } else {
        ++alpha;
      }
    }
    string curr;
    set<string> ans;
    function<void(int, int)> dfs = [&](int i, int j) -> void {
      if (i == s.size()) {
        if (j == 0 && curr.size() == pair * 2 + alpha) {
          ans.insert(curr);
        }
        return;
      }

      if (s[i] == '(') {
        dfs(i + 1, j);

        curr.push_back('(');
        dfs(i + 1, j + 1);
        curr.pop_back();
      } else if (s[i] == ')') {
        dfs(i + 1, j);

        if (j > 0) {
          curr.push_back(')');
          dfs(i + 1, j - 1);
          curr.pop_back();
        }
      } else {
        curr.push_back(s[i]);
        dfs(i + 1, j);
        curr.pop_back();
      }
    };
    dfs(0, 0);
    return {begin(ans), end(ans)};
  }
};
