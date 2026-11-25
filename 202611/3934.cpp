class Solution {
public:
  int smallestUniqueSubarray(vector<int> &nums) {
    const int base = 53;
    const int MOD = 1e9 + 7;
    int n = nums.size();
    vector<long long> pow(n + 1);
    pow[0] = 1;
    for (int i = 1; i <= n; ++i) {
      pow[i] = pow[i - 1] * base % MOD;
    }

    auto ok = [&](int v) {
      if (v == n)
        return true;
      unordered_map<long long, int> freq;
      long long h = 0;
      for (int i = 0; i < v; ++i) {
        h = (nums[i] + h * base) % MOD;
      }
      freq[h] = 1;
      for (int i = v; i < n; ++i) {
        h = (h - nums[i - v] * pow[v - 1] % MOD + MOD) % MOD;
        h = (h * base + nums[i]) % MOD;
        ++freq[h];
      }
      for (auto [_, v] : freq) {
        if (v == 1)
          return true;
      }
      return false;
    };

    int lo = 1, hi = n;
    int ans = -1;
    while (lo <= hi) {
      int mid = lo + hi >> 1;
      if (ok(mid)) {
        ans = mid;
        hi = mid - 1;
      } else {
        lo = mid + 1;
      }
    }
    return ans;
  }
};
