class Solution {
public:
  vector<int> findMissingElements(vector<int> &nums) {
    sort(begin(nums), end(nums));
    int curr = nums[0];
    vector<int> ans;
    for (int j = 0; j < nums.size(); ++j) {
      while (curr < nums[j]) {
        ans.push_back(curr++);
      }
      curr++;
    }
    return ans;
  }
};
