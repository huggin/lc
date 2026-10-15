class Solution {
public:
  int sumCounts(vector<int> &nums) {
    int ans = 0;
    int n = nums.size();
    for (int i = 0; i < n; ++i) {
      for (int j = i; j < n; ++j) {
        int unique = 0;
        int cnt[101] = {0};
        for (int k = i; k <= j; ++k) {
          if (cnt[nums[k]]++ == 0) {
            ++unique;
          }
        }
        ans += unique * unique;
      }
    }
    return ans;
  }
};
