class Solution {
public:
  long long countNonDecreasingSubarrays(vector<int> &nums, int k) {
    int n = nums.size();
    long long c = k;
    long long ans = 0;
    int j = n - 1;

    deque<pair<int, int>> st;

    for (int i = n - 1; i >= 0; i--) {
      while (j >= 0 && c >= 0) {
        if (st.empty() || nums[j] < st.back().first) {
          st.push_back({nums[j], 1});
        } else {
          int total = 1;

          while (!st.empty() && nums[j] >= st.back().first) {
            total += st.back().second;
            c -= 1LL * (nums[j] - st.back().first) * st.back().second;
            st.pop_back();
          }

          st.push_back({nums[j], total});
        }
        j--;
      }

      if (c < 0) {
        ans += i - j - 1;
      } else {
        ans += i - j;
      }

      c += st.front().first - nums[i];
      st.front().second--;

      if (st.front().second == 0) {
        st.pop_front();
      }
    }

    return ans;
  }
};
