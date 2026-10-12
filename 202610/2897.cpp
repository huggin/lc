class Solution {
public:
  int maxSum(vector<int> &nums, int k) {
    int cnt[32] = {0};
    for (int num : nums) {
      for (int i = 0; i < 32; ++i) {
        cnt[i] += !!(num & (1 << i));
      }
    }
    vector<long long> a(k);
    for (int i = 30; i >= 0; --i) {
      for (int j = 0; j < k; ++j) {
        if (cnt[i]-- > 0) {
          a[j] |= (1 << i);
        }
      }
    }
    long long ans = 0;
    const int MOD = 1e9 + 7;
    for (int i = 0; i < k; ++i) {
      ans = (ans + a[i] * a[i]) % MOD;
    }
    return ans;
  }
};
