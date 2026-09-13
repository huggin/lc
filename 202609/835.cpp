class Solution {
public:
  int largestOverlap(vector<vector<int>> &img1, vector<vector<int>> &img2) {
    int n = img1.size();
    int ans = 0;
    auto f = [=](int i1, int j1, const vector<vector<int>> &img1,
                 const vector<vector<int>> &img2) {
      int ans = 0;
      for (int i = i1; i < n; ++i) {
        for (int j = j1; j < n; ++j) {
          if (img1[i][j] == 1 && img2[i - i1][j - j1] == 1)
            ++ans;
        }
      }
      return ans;
    };

    auto f2 = [=](int i1, int j1, const vector<vector<int>> &img1,
                  const vector<vector<int>> &img2) {
      int ans = 0;
      for (int i = 0; i <= i1; ++i) {
        for (int j = j1; j < n; ++j) {
          if (img1[i][j] == 1 && img2[n - 1 - i1 + i][j - j1] == 1)
            ++ans;
        }
      }
      return ans;
    };

    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < n; ++j) {
        ans = max(ans, f(i, j, img1, img2));
        ans = max(ans, f(i, j, img2, img1));
        ans = max(ans, f2(i, j, img1, img2));
        ans = max(ans, f2(i, j, img2, img1));
      }
    }
    return ans;
  }
};
