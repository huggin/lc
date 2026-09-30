class Solution {
public:
  vector<int> maxDepthAfterSplit(string seq) {
    int n = seq.size();
    vector<int> ans(n);
    int cnt = 0;
    for (int i = 0; i < n; ++i) {
      if (seq[i] == '(') {
        ++cnt;
      } else {
        --cnt;
      }
      ans[i] = seq[i] == '(' ? cnt % 2 : 1 - cnt % 2;
    }
    return ans;
  }
};
