class Solution {
public:
  long long minSumSquareDiff(vector<int> &nums1, vector<int> &nums2, int k1,
                             int k2) {
    int n = nums1.size();
    vector<int> diff(n);
    for (int i = 0; i < n; ++i) {
      diff[i] = abs(nums1[i] - nums2[i]);
    }
    sort(begin(diff), end(diff));
    vector<pair<int, int>> vp;
    int i = 0;
    while (i < n) {
      int j = i;
      while (j < n && diff[j] == diff[i])
        ++j;
      if (diff[i] > 0) {
        vp.emplace_back(diff[i], j - i);
      }
      i = j;
    }
    if (vp.size() == 0)
      return 0;
    long long k = k1 + k2;
    while (k > 0) {
      auto [d, c] = vp.back();
      if (d == 0)
        break;
      vp.pop_back();
      int d2 = 0;
      int c2 = 0;
      if (vp.size() != 0) {
        d2 = vp.back().first;
        c2 = vp.back().second;
      }
      if (1LL * (d - d2) * c <= k) {
        k -= 1LL * (d - d2) * c;
        if (c2 != 0)
          vp.pop_back();
        vp.emplace_back(d2, c + c2);
      } else {
        int div = k / c;
        int rem = k % c;
        vp.emplace_back(d - div - 1, rem);
        vp.emplace_back(d - div, c - rem);
        break;
      }
    }
    long long ans = 0;
    for (auto [d, c] : vp) {
      ans += 1LL * d * d * c;
    }
    return ans;
  }
};
