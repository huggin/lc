class Solution {
public:
  int largestInteger(vector<int> &nums, int k) {
    int n = nums.size();
    if (k == n) {
      return *max_element(begin(nums), end(nums));
    }
    array<int, 51> cnt;
    if (k == 1) {
      for (int num : nums) {
        ++cnt[num];
      }
      int ans = -1;
      for (int i = 50; i > 0; --i) {
        if (cnt[i] == 1)
          return i;
      }
      return -1;
    }
    int a = nums[0];
    int b = nums[n - 1];
    for (int i = 0; i < k; ++i) {
      ++cnt[nums[i]];
    }
    int ca = 0, cb = 0;
    if (cnt[a] > 0)
      ++ca;
    if (cnt[b] > 0)
      ++cb;
    for (int i = k; i < n; ++i) {
      --cnt[nums[i - k]];
      ++cnt[nums[i]];
      if (cnt[a] > 0)
        ++ca;
      if (cnt[b] > 0)
        ++cb;
    }
    if (ca > 1 && cb > 1)
      return -1;
    if (ca == 1 && cb == 1)
      return max(a, b);
    if (ca == 1)
      return a;
    return b;
  }
};
