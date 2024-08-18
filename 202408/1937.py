class Solution {
public:
    long long maxPoints(vector<vector<int>>& points) {
        long long ans = 0;
        int n = points.size();
        int m = points[0].size();
        vector<long long> dp(m), ndp(m);
        for(int i = 0; i < m; i++) dp[i] = points[0][i];

        for(int i = 1; i < n; i++) {
            multiset<long long> s1, s2;
            for(int j = 0; j < m; j++) {
                s2.insert(dp[j] - j);
            }
            for(int j = 0; j < m; j++) {
                ndp[j] = dp[j];
                if (s2.size() > 0) 
                    ndp[j] = max(ndp[j], *s2.rbegin() + j);
                if (s1.size() > 0)
                    ndp[j] = max(ndp[j], *s1.rbegin() + m - 1 - j);
                s2.erase(s2.find(dp[j] - j));
                s1.insert(dp[j] - (m-1-j));
                ndp[j] += points[i][j];
            }
            std::swap(dp, ndp);
        }
        return *max_element(dp.begin(), dp.end());
    }
};
