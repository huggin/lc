class Solution {
  int dp[101][101];
  int dp2[101][101];

public:
  vector<int> pathsWithMaxScore(vector<string> &board) {
    const int MOD = int(1e9 + 7);
    int n = board.size();
    memset(dp, 0, sizeof(dp));
    memset(dp2, 0, sizeof(dp2));
    for (int i = n - 1; i >= 0; --i) {
      for (int j = n - 1; j >= 0; --j) {
        int v = 0;
        if (board[i][j] == 'S') {
          dp2[i][j] = 1;
        } else if (board[i][j] == 'X') {
          continue;
        } else if (isdigit(board[i][j])) {
          v = board[i][j] - '0';
        }

        if (i + 1 < n && dp2[i + 1][j] > 0) {
          if (dp[i][j] < dp[i + 1][j] + v) {
            dp[i][j] = dp[i + 1][j] + v;
            dp2[i][j] = dp2[i + 1][j];
          } else if (dp[i][j] == dp[i + 1][j] + v) {
            dp2[i][j] += dp2[i + 1][j];
            if (dp2[i][j] >= MOD)
              dp2[i][j] -= MOD;
          }
        }
        if (j + 1 < n && dp2[i][j + 1] > 0) {
          if (dp[i][j] < dp[i][j + 1] + v) {
            dp[i][j] = dp[i][j + 1] + v;
            dp2[i][j] = dp2[i][j + 1];
          } else if (dp[i][j] == dp[i][j + 1] + v) {
            dp2[i][j] += dp2[i][j + 1];
            if (dp2[i][j] >= MOD)
              dp2[i][j] -= MOD;
          }
        }
        if (i + 1 < n && j + 1 < n && dp2[i + 1][j + 1] > 0) {
          if (dp[i][j] < dp[i + 1][j + 1] + v) {
            dp[i][j] = dp[i + 1][j + 1] + v;
            dp2[i][j] = dp2[i + 1][j + 1];
          } else if (dp[i][j] == dp[i + 1][j + 1] + v) {
            dp2[i][j] += dp2[i + 1][j + 1];
            if (dp2[i][j] >= MOD)
              dp2[i][j] -= MOD;
          }
        }
      }
    }

    return {dp[0][0], dp2[0][0]};
  }
};
