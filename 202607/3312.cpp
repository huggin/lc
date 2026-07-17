class Solution {
public:
  vector<int> gcdValues(vector<int> &nums, vector<long long> &queries) {
    int ma = *max_element(begin(nums), end(nums));
    vector<int> cnt(ma + 1);
    for (int num : nums) {
      ++cnt[num];
    }
    for (int i = 1; i <= ma; ++i) {
      for (int j = i * 2; j <= ma; j += i) {
        cnt[i] += cnt[j];
      }
    }
    vector<long long> ps(ma + 1);
    for (int i = ma; i > 0; --i) {
      ps[i] = 1LL * cnt[i] * (cnt[i] - 1) / 2;
      for (int j = i * 2; j <= ma; j += i) {
        ps[i] -= ps[j];
      }
    }
    for (int i = 1; i <= ma; ++i) {
      ps[i] += ps[i - 1];
    }
    int n = queries.size();
    vector<int> ans(n);
    for (int i = 0; i < n; ++i) {
      ans[i] = upper_bound(begin(ps), end(ps), queries[i]) - begin(ps);
    }
    return ans;
  }
};
