class Solution {
  long long lcm(const std::vector<long long> &v) {
    return std::accumulate(
        v.begin(), v.end(), 1LL,
        [](long long a, long long b) { return std::lcm(a, b); });
  }

public:
  long long findKthSmallest(vector<int> &coins, int k) {
    sort(begin(coins), end(coins));
    int n = coins.size();
    vector<int> filter(n);
    vector<int> nums;

    for (int i = 0; i < n; ++i) {
      if (!filter[i]) {
        nums.push_back(coins[i]);
        for (int j = i + 1; j < n; ++j) {
          if (coins[j] % coins[i] == 0) {
            filter[j] = 1;
          }
        }
      }
    }

    n = nums.size();
    vector<long long> curr;
    vector<pair<long long, int>> pc_lcm;
    function<void(int)> f = [&](int k) {
      if (k == n) {
        if (curr.size() > 0) {
          pc_lcm.emplace_back(lcm(curr), curr.size() % 2 ? 1 : -1);
        }
        return;
      }
      curr.push_back(nums[k]);
      f(k + 1);
      curr.pop_back();
      f(k + 1);
    };
    f(0);
    sort(begin(pc_lcm), end(pc_lcm));

    auto ok = [&](long long v, int k) -> bool {
      long long ans = 0;
      for (int i = 0; i < pc_lcm.size(); ++i) {
        if (pc_lcm[i].first > v)
          break;
        ans += v / pc_lcm[i].first * pc_lcm[i].second;
      }
      return ans >= k;
    };

    long long lo = nums[0], hi = 1LL * nums[0] * k;
    long long ans = -1;
    while (lo <= hi) {
      long long mi = (lo + hi) >> 1;
      if (ok(mi, k)) {
        ans = mi;
        hi = mi - 1;
      } else {
        lo = mi + 1;
      }
    }
    return ans;
  }
};
