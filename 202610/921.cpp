class Solution {
public:
  int minAddToMakeValid(string s) {
    int ans = 0;
    stack<char> sc;
    for (char c : s) {
      if (c == '(') {
        sc.push(c);
      } else if (sc.empty()) {
        ++ans;
      } else {
        sc.pop();
      }
    }
    return ans + sc.size();
  }
};
