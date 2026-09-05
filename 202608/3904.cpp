class Solution {
public:
  int firstStableIndex(vector<int> &nums, int k) {
    int n = nums.size();
    vector<int> small(n);
    small[n - 1] = nums[n - 1];
    for (int i = n - 2; i >= 0; --i) {
      small[i] = min(nums[i], small[i + 1]);
    }
    int large = 0;
    for (int i = 0; i < n; ++i) {
      large = max(large, nums[i]);
      int curr = large - small[i];
      if (curr <= k)
        return i;
    }

    return -1;
  }
};
