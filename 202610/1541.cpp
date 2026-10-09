class Solution {
public:
  int minInsertions(string s) {
    stack<int> si;
    int ans = 0;
    for (char c : s) {
      if (c == '(') {
        if (!si.empty() && si.top() == 1) {
          ++ans;
          si.pop();
        }
        si.push(2);
      } else if (si.empty()) {
        ++ans;
        si.push(1);
      } else {
        if (si.top() == 2) {
          si.pop();
          si.push(1);
        } else {
          si.pop();
        }
      }
    }
    while (!si.empty()) {
      ans += si.top();
      si.pop();
    }
    return ans;
  }
};
