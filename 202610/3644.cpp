class Solution {
public:
  int sortPermutation(vector<int> &nums) {
    const int mask = (1 << 30) - 1;
    int ans = mask;
    for (auto [k, v] : views::enumerate(nums)) {
      if (k != v) {
        ans &= v;
      }
    }
    return ans == mask ? 0 : ans;
  }
};
