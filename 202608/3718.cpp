class Solution {
public:
  int missingMultiple(vector<int> &nums, int k) {
    unordered_set<int> s(begin(nums), end(nums));
    int ans = k;
    while (s.find(ans) != end(s)) {
      ans += k;
    }
    return ans;
  }
};
