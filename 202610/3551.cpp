class Solution {
  int sum(int b) {
    int cnt = 0;
    while (b > 0) {
      cnt += b % 10;
      b /= 10;
    }
    return cnt;
  }

public:
  int minSwaps(vector<int> &nums) {
    vector<pair<int, int>> a;
    for (auto [k, v] : views::enumerate(nums)) {
      a.emplace_back(sum(v), v);
    }
    sort(begin(a), end(a));
    unordered_map<int, int> target;
    for (auto [k, v] : views::enumerate(a)) {
      target[v.second] = k;
    }

    int ans = 0;
    int n = nums.size();
    vector<bool> visited(n);
    for (int i = 0; i < n; ++i) {
      if (visited[i] || target[nums[i]] == i) {
        continue;
      }
      int size = 0;
      int j = i;
      while (!visited[j]) {
        visited[j] = true;
        j = target[nums[j]];
        ++size;
      }
      ans += size - 1;
    }
    return ans;
  }
};
