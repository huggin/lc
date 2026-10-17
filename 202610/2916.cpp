class Fenwick {
  using ll = long long;
  const int MOD = 1e9 + 7;
  vector<ll> bit1, bit2;

public:
  Fenwick(int n) {
    bit1.assign(n + 1, 0);
    bit2.assign(n + 1, 0);
  }

  ll query1(int k) {
    ll ans = 0;
    for (++k; k > 0; k -= k & -k) {
      ans += bit1[k];
      if (ans >= MOD)
        ans -= MOD;
    }
    return ans;
  }

  ll query2(int k) {
    ll ans = 0;
    for (++k; k > 0; k -= k & -k) {
      ans += bit2[k];
      if (ans >= MOD)
        ans -= MOD;
    }
    return ans;
  }

  ll query(int k) { return (query1(k) * k % MOD - query2(k) + MOD) % MOD; }

  ll query(int i, int j) { return (query(j) - query(i - 1) + MOD) % MOD; }

  void add1(int k, int v) {
    for (++k; k < bit1.size(); k += k & -k) {
      bit1[k] += v;
    }
  }

  void add2(int k, int v) {
    for (++k; k < bit2.size(); k += k & -k) {
      bit2[k] += v;
    }
  }

  void add(int i, int j, ll v) {
    add1(i, v);
    add1(j + 1, -v);
    add2(i, v * (i - 1));
    add2(j + 1, -v * j);
  }
};

class Solution {
  using ll = long long;

public:
  int sumCounts(vector<int> &nums) {
    int n = nums.size();
    Fenwick fen(n);
    const int MOD = 1e9 + 7;
    ll ans = 0, cur = 0;
    unordered_map<int, int> seen;
    for (auto [i, v] : views::enumerate(nums)) {
      int j = (seen.count(v) ? seen[v] : -1) + 1;
      ll q = fen.query(j, i);
      cur = (cur + q * 2 + i - j + 1) % MOD;
      ans = (ans + cur) % MOD;
      fen.add(j, i, 1);
      seen[v] = i;
    }
    return ans;
  }
};
