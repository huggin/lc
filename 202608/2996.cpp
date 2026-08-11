class Solution {
public:
  int missingInteger(vector<int> &nums) {
    int curr = nums[0];
    for (int i = 1; i < nums.size(); ++i) {
      if (nums[i] == nums[i - 1] + 1) {
        curr += nums[i];
      } else {
        break;
      }
    }
    unordered_set<int> s(begin(nums), end(nums));
    while (s.find(curr) != end(s)) {
      ++curr;
    }
    return curr;
  }
};
