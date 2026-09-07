class Solution {
public:
  int distinctSubseqII(string s) {
    const int MOD = 1'000'000'007;
    array<long long, 26> dp;
    for (char c : s) {
      int tt = reduce(begin(dp), end(dp), 1LL) % MOD;
      dp[c - 'a'] = tt;
    }
    return reduce(begin(dp), end(dp), 0LL) % MOD;
  }
};
