class Solution {
public:
  int scoreOfParentheses(string s) {
    stack<int> si;
    unordered_map<int, int> pairs;
    for (auto [i, c] : views::enumerate(s)) {
      if (c == '(') {
        si.push(i);
      } else {
        pairs[i] = si.top();
        si.pop();
      }
    }
    stack<pair<int, int>> sp;
    for (auto [i, c] : views::enumerate(s)) {
      if (c == '(') {
        sp.emplace(i, 0);
      } else if (pairs[i] == i - 1) {
        sp.pop();
        sp.emplace(i, 1);
      } else {
        int temp = 0;
        do {
          temp += sp.top().second;
          sp.pop();
        } while (pairs[i] != sp.top().first);
        temp += sp.top().second;
        int k = sp.top().first;
        sp.pop();
        sp.emplace(k, temp * 2);
      }
    }
    int ans = 0;
    while (!sp.empty()) {
      ans += sp.top().second;
      sp.pop();
    }
    return ans;
  }
};
