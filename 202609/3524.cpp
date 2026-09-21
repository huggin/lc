class Solution {
public:
  vector<long long> resultArray(vector<int> &nums, int k) {
    vector<int> a;
    a.reserve(nums.size());

    for (int x : nums) {
      a.push_back(x % k);
    }

    vector<long long> ans(k, 0);
    vector<int> dp(k);

    for (int i = 0; i < a.size(); ++i) {
      vector<int> dp2(k);

      for (int j = 0; j < k; ++j) {
        dp2[j * a[i] % k] += dp[j];
      }

      dp2[a[i]] += 1;

      for (int j = 0; j < k; ++j) {
        ans[j] += dp2[j];
      }

      dp = std::move(dp2);
    }

    return ans;
  }
};
