class Solution {
public:
  vector<int> leftRightDifference(vector<int> &nums) {
    int sum = reduce(begin(nums), end(nums));
    int n = nums.size();
    vector<int> ans(n);
    int left = 0, right = sum;
    for (int i = 0; i < n; ++i) {
      right -= nums[i];
      ans[i] = abs(left - right);
      left += nums[i];
    }
    return ans;
  }
};
