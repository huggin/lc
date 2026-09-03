class Solution {
public:
  bool uniformArray(vector<int> &nums1) {
    if (nums1.size() == 1)
      return true;
    sort(begin(nums1), end(nums1));
    if (nums1[0] % 2 == 0 && nums1[1] % 2 == 1)
      return false;
    if (nums1[0] % 2 == 0) {
      return all_of(nums1.begin(), nums1.end(),
                    [](int x) { return x % 2 == 0; });
    }
    return true;
  }
};
