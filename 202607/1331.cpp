class Solution {
public:
  vector<int> arrayRankTransform(vector<int> &arr) {
    vector<int> sorted(arr);
    sort(begin(sorted), end(sorted));
    sorted.erase(unique(begin(sorted), end(sorted)), end(sorted));
    vector<int> ans(arr.size());
    for (auto [i, x] : std::views::enumerate(arr)) {
      ans[i] = lower_bound(begin(sorted), end(sorted), x) - sorted.begin() + 1;
    }
    return ans;
  }
};
