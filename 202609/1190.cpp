class Solution {
  string ans;
  unordered_map<int, int> pairs;
  stack<int> ss;
  string s;

  void go(int i, int j, bool rev) {
    if (i > j)
      return;
    if (!rev) {
      int k = i;
      while (k <= j) {
        if (s[k] == '(') {
          go(i + 1, pairs[k] - 1, !rev);
          k = pairs[k] + 1;
        } else if (s[k] == ')') {
          return;
        } else {
          ans.push_back(s[k]);
          ++k;
        }
      }
    } else {
      int k = j;
      while (k >= i) {
        if (s[k] == ')') {
          go(pairs[k] + 1, k - 1, !rev);
          k = pairs[k] - 1;
        } else if (s[k] == '(') {
          return;
        } else {
          ans.push_back(s[k]);
          --k;
        }
      }
    }
  }

public:
  string reverseParentheses(string s) {
    for (auto [k, c] : std::views::enumerate(s)) {
      if (c == '(') {
        ss.push(k);
      } else if (c == ')') {
        int left = ss.top();
        ss.pop();
        pairs[left] = k;
        pairs[k] = left;
      }
    }
    this->s = s;
    go(0, s.size() - 1, false);
    return ans;
  }
};
