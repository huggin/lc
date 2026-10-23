class Solution {
public:
  int minOperations(vector<int> &nums) {
    int n = nums.size();
    int i = find(begin(nums), end(nums), 0) - begin(nums);
    int j = i + 1;
    if (j == n)
      j = 0;
    int curr = 1;
    while (nums[j] == curr && j != i) {
      ++curr;
      if (++j == n)
        j = 0;
    }
    int ans = n;
    if (j == i) {
      return min(i, n - i + 2);
    }
    j = i - 1;
    if (j == -1)
      j = n - 1;
    curr = 1;
    while (nums[j] == curr && j != i) {
      ++curr;
      if (--j == -1)
        j = n - 1;
    }
    if (j == i) {
      return min(i + 2, n - i);
    }
    return -1;
  }
};
