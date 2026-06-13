class Solution {
public:
  string mapWordWeights(vector<string> &words, vector<int> &weights) {
    string ans;
    for (const string &word : words) {
      int cnt = 0;
      for (char c : word) {
        cnt += weights[c - 'a'];
      }
      ans.push_back('z' - cnt % 26);
    }
    return ans;
  }
};
