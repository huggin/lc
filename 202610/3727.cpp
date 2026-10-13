class Solution {
public:
  long long maxAlternatingSum(vector<int> &nums) {
    sort(begin(nums), end(nums), [](int l, int r) { return abs(l) < abs(r); });
    int i = 0, j = nums.size() - 1;
    long long ans = 0;
    while (i < j) {
      ans += 1LL * nums[j] * nums[j] - 1LL * nums[i] * nums[i];
      ++i;
      --j;
    }
    if (i == j)
      ans += 1LL * nums[i] * nums[i];
    return ans;
  }
};
