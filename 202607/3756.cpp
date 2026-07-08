class Solution {
  using ll = long long;
  const int MOD = int(1e9 + 7);
  ll pow(int b, ll a = 10) {
    ll ans = 1;
    while (b) {
      if (b & 1) {
        ans = (ans * a) % MOD;
      }
      b >>= 1;
      a = (a * a) % MOD;
    }
    return ans;
  }

public:
  vector<int> sumAndMultiply(string s, vector<vector<int>> &queries) {
    vector<ll> pre{0}, pre2{0}, time{0};
    for (char c : s) {
      int d = c - '0';
      pre.push_back(pre.back() + d);
      if (d != 0) {
        pre2.push_back((pre2.back() * 10 + d) % MOD);
        time.push_back(time.back() + 1);
      } else {
        pre2.push_back(pre2.back());
        time.push_back(time.back());
      }
    }
    vector<int> ans;
    for (const auto &q : queries) {
      int i = q[0];
      int j = q[1] + 1;
      ans.push_back((pre2[j] - pre2[i] * pow(time[j] - time[i]) % MOD + MOD) %
                    MOD * (pre[j] - pre[i]) % MOD);
    }
    return ans;
  }
};
