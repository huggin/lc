class Solution {
  int f(const vector<int> &a, const vector<int> &b, const vector<int> &c,
        const vector<int> &d) {
    int first = numeric_limits<int>::max();
    int ans = first;
    for (int i = 0; i < a.size(); ++i) {
      first = min(first, a[i] + b[i]);
    }
    for (int i = 0; i < c.size(); ++i) {
      if (c[i] >= first) {
        ans = min(ans, c[i] + d[i]);
      } else {
        ans = min(ans, first + d[i]);
      }
    }
    return ans;
  }

public:
  int earliestFinishTime(vector<int> &landStartTime, vector<int> &landDuration,
                         vector<int> &waterStartTime,
                         vector<int> &waterDuration) {
    return min(f(landStartTime, landDuration, waterStartTime, waterDuration),
               f(waterStartTime, waterDuration, landStartTime, landDuration));
  }
};
