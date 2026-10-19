class Solution {
public:
  vector<int> targetIndices(vector<int> &nums, int target) {
    sort(begin(nums), end(nums));
    auto hi = upper_bound(begin(nums), end(nums), target);
    auto lo = lower_bound(begin(nums), end(nums), target);
    vector<int> ans;
    for (auto it = lo; it != hi; ++it) {
      ans.push_back(it - begin(nums));
    }
    return ans;
  }
};
