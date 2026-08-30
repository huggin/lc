class Solution {
public:
  int minimumDeletions(vector<int> &nums) {
    if (nums.size() == 1)
      return 1;
    auto [min_it, max_it] = std::minmax_element(nums.begin(), nums.end());
    int a = min_it - nums.begin(), b = max_it - nums.begin();
    if (a > b)
      swap(a, b);
    int n = nums.size();
    int ans = min(b + 1, n - a);
    return min(ans, a + 1 + n - b);
  }
};
