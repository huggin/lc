class Solution {
public:
  vector<int> lexicographicallySmallestArray(vector<int> &nums, int limit) {
    vector<int> sorted(nums);
    sort(begin(sorted), end(sorted));
    int n = nums.size();
    unordered_map<int, vector<int>> groups;
    unordered_map<int, int> item_2_groups;
    int group = -1;
    for (int i = 0; i < n; ++i) {
      if (i == 0 || sorted[i] > sorted[i - 1] + limit) {
        ++group;
      }
      item_2_groups[sorted[i]] = group;
      groups[group].push_back(sorted[i]);
    }
    vector<int> ans(n);
    unordered_map<int, int> group_idx;
    for (int i = 0; i < n; ++i) {
      group = item_2_groups[nums[i]];
      ans[i] = groups[group][group_idx[group]++];
    }
    return ans;
  }
};
