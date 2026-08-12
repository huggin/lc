class Solution {
public:
  int maxSubarrayLength(vector<int> &nums, int k) {
    int ans = 0;
    int j = 0;
    unordered_map<int, int> cnt;
    for (int i = 0; i < nums.size(); ++i) {
      ++cnt[nums[i]];
      while (cnt[nums[i]] > k) {
        --cnt[nums[j++]];
      }
      ans = max(ans, i - j + 1);
    }
    return ans;
  }
};
