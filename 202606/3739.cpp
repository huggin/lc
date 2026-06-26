class Fenwick {
public:
  Fenwick(int m) : n(m + 1) { bit.resize(n); }
  void update(int k, int d) {
    for (++k; k < n; k += k & -k) {
      bit[k] += d;
    }
  }

  int get(int k) {
    int ans = 0;
    for (++k; k > 0; k -= k & -k) {
      ans += bit[k];
    }
    return ans;
  }

private:
  int n;
  vector<int> bit;
};

class Solution {
public:
  long long countMajoritySubarrays(vector<int> &nums, int target) {
    int n = nums.size();
    vector<int> pref(n + 1);
    for (int i = 0; i < n; ++i) {
      pref[i + 1] = pref[i] + (nums[i] == target ? 1 : -1);
    }
    vector<int> vals(begin(pref), end(pref));
    sort(begin(vals), end(vals));
    vals.erase(unique(begin(vals), end(vals)), end(vals));
    for (int i = 0; i <= n; ++i) {
      pref[i] = lower_bound(begin(vals), end(vals), pref[i]) - begin(vals);
    }
    int m = *max_element(begin(pref), end(pref));
    long long ans = 0;
    Fenwick fen(m);
    for (int i = 0; i <= n; ++i) {
      if (pref[i] > 0)
        ans += fen.get(pref[i] - 1);
      fen.update(pref[i], 1);
    }

    return ans;
  }
};
