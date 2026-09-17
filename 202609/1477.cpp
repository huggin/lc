class Solution {
public:
  int minSumOfLengths(vector<int> &arr, int target) {
    int n = arr.size();
    vector<int> left(n, n);
    int curr = 0;
    int j = 0;
    for (int i = 0; i < n; ++i) {
      curr += arr[i];
      while (curr > target) {
        curr -= arr[j++];
      }
      if (curr == target) {
        left[i] = i - j + 1;
      }
      if (i > 0)
        left[i] = min(left[i - 1], left[i]);
    }
    vector<int> right(n, n);
    j = n - 1;
    curr = 0;
    for (int i = n - 1; i >= 0; --i) {
      curr += arr[i];
      while (curr > target) {
        curr -= arr[j--];
      }
      if (curr == target) {
        right[i] = j - i + 1;
      }
      if (i < n - 1)
        right[i] = min(right[i + 1], right[i]);
    }
    int ans = n + 1;
    for (int i = 0; i < n - 1; ++i) {
      if (left[i] != -1 && right[i + 1] != -1) {
        ans = min(ans, left[i] + right[i + 1]);
      }
    }

    return ans <= n ? ans : -1;
  }
};
