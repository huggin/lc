class Solution {
  int st1[25][50010];
  int st2[25][50010];
  int log2_floor(unsigned long i) { return std::bit_width(i) - 1; }
  int get(int l, int r) {
    int i = log2_floor(r - l + 1);
    int mi = min(st1[i][l], st1[i][r - (1 << i) + 1]);
    int ma = max(st2[i][l], st2[i][r - (1 << i) + 1]);
    return ma - mi;
  }

public:
  long long maxTotalValue(vector<int> &nums, int k) {
    const int K = 25;
    const int n = nums.size();
    copy(begin(nums), end(nums), st1[0]);
    copy(begin(nums), end(nums), st2[0]);
    for (int i = 1; i < K; ++i) {
      for (int j = 0; j + (1 << i) <= n; ++j) {
        st1[i][j] = min(st1[i - 1][j], st1[i - 1][j + (1 << (i - 1))]);
        st2[i][j] = max(st2[i - 1][j], st2[i - 1][j + (1 << (i - 1))]);
      }
    }
    long long ans = 0;
    priority_queue<tuple<int, int, int>> pq;
    for (int l = 0; l < n; ++l) {
      pq.emplace(get(l, n - 1), l, n - 1);
    }
    for (int i = 0; i < k; ++i) {
      auto [v, l, r] = pq.top();
      ans += v;
      pq.pop();
      if (l < r) {
        pq.emplace(get(l, r - 1), l, r - 1);
      }
    }
    return ans;
  }
};
