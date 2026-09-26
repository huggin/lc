class Solution {
public:
  string evaluate(string s, vector<vector<string>> &knowledge) {
    unordered_map<string, string> m;
    for (const auto &kv : knowledge) {
      m[kv[0]] = kv[1];
    }
    string ans;
    int i = 0;
    while (i < s.size()) {
      if (s[i] == '(') {
        auto j = s.find(')', i + 1);
        string key = s.substr(i + 1, j - i - 1);
        if (m.find(key) == m.end()) {
          ans.push_back('?');
        } else {
          ans += m[key];
        }
        i = j + 1;
      } else {
        ans.push_back(s[i]);
        ++i;
      }
    }
    return ans;
  }
};
