class Solution {
public:
  int numOfWays(vector<int> &nums) {
    const int MOD = 1e9 + 7;
    int n = nums.size();
    vector<vector<long long>> c(n + 1, vector<long long>(n + 1, 1));
    for (int i = 2; i <= n; ++i) {
      for (int j = 1; j < i; ++j) {
        c[i][j] = c[i - 1][j - 1] + c[i - 1][j];
        if (c[i][j] >= MOD)
          c[i][j] -= MOD;
      }
    }
    long long ans = 1;
    set<int> seen{0, n + 1};
    auto f = [&](int k) -> pair<int, int> {
      auto it = seen.lower_bound(nums[k]);
      int hi = *it;
      int lo = *(--it);
      int small = 0, large = 0;
      for (int i = k + 1; i < n; ++i) {
        if (nums[i] > nums[k] && nums[i] < hi) {
          ++large;
        } else if (nums[i] < nums[k] && nums[i] > lo) {
          ++small;
        }
      }
      seen.insert(nums[k]);
      return {small, large};
    };
    vector<pair<int, int>> sl;
    for (int i = 0; i < n; ++i) {
      auto [s, l] = f(i);
      ans = (ans * c[s + l][s]) % MOD;
    }
    return ans - 1;
  }
};
