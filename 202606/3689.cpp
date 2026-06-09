class Solution {
public:
  long long maxTotalValue(vector<int> &nums, int k) {
    auto [min_it, max_it] = std::minmax_element(begin(nums), end(nums));
    return 1LL * (*max_it - *min_it) * k;
  }
};
