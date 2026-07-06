class Solution {
public:
  int removeCoveredIntervals(vector<vector<int>> &intervals) {
    sort(begin(intervals), end(intervals),
         [](const vector<int> &l, const vector<int> &r) {
           if (l[0] < r[0] || l[0] == r[0] && l[1] >= r[1]) {
             return 1;
           }
           return 0;
         });
    int right = intervals[0][1];
    int removed = 0;
    for (int i = 1; i < intervals.size(); ++i) {
      if (intervals[i][1] <= right) {
        ++removed;
      } else {
        right = intervals[i][1];
      }
    }
    return intervals.size() - removed;
  }
};
