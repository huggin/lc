class Solution {
    int f(const vector<int>& a, const vector<int>& b, const vector<int>& c, const vector<int>& d) {
        int ans = numeric_limits<int>::max();
        for(int i = 0; i < a.size(); ++i) {
            int curr = a[i] + b[i];
            for(int j = 0; j < c.size(); ++j) {
                if (c[j] <= curr) {
                    ans = min(ans, curr + d[j]);
                } else {
                    ans = min(ans, c[j] + d[j]);
                }
            }
        }
        return ans;
    }
public:
    int earliestFinishTime(vector<int>& landStartTime, vector<int>& landDuration, vector<int>& waterStartTime, vector<int>& waterDuration) {
        return min(
            f(landStartTime, landDuration, waterStartTime, waterDuration), 
            f(waterStartTime, waterDuration, landStartTime, landDuration)
        );
    }
};
