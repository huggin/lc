class Solution {
public:
  int countDaysTogether(string arriveAlice, string leaveAlice, string arriveBob,
                        string leaveBob) {
    vector<int> days{0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    string start = max(arriveAlice, arriveBob);
    string end = min(leaveAlice, leaveBob);
    if (start > end)
      return 0;
    int sm, sd, em, ed;
    sscanf(start.c_str(), "%d-%d", &sm, &sd);
    sscanf(end.c_str(), "%d-%d", &em, &ed);
    int ans = 0;
    for (int i = sm; i <= em; ++i) {
      int d1 = i == sm ? sd : 1;
      int d2 = i == em ? ed : days[i];
      ans += d2 - d1 + 1;
    }
    return ans;
  }
};
