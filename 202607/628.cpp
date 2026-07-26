class Solution {
public:
  int maximumProduct(vector<int> &nums) {
    sort(begin(nums), end(nums));
    int n = nums.size();
    int v1 = nums[0] * nums[1] * nums[n - 1];
    int v2 = nums[0] * nums[n - 2] * nums[n - 1];
    int v3 = nums[n - 3] * nums[n - 2] * nums[n - 1];
    return max({v1, v2, v3});
  }
};
