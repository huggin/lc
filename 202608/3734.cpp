class Solution {
public:
  string lexPalindromicPermutation(string s, string target) {
    array<int, 26> cnt;
    for (char c : s) {
      ++cnt[c - 'a'];
    }
    int odd = 0;
    char c = ' ';
    for (int i = 0; i < 26; ++i) {
      if (cnt[i] & 1) {
        ++odd;
        c = 'a' + i;
      }
    }
    if (odd > 1)
      return "";
    int n = s.size();
    string first;
    array<int, 26> cnt2(cnt);
    for (int i = 25; i >= 0; --i) {
      while (cnt2[i] >= 2) {
        first.push_back('a' + i);
        cnt2[i] -= 2;
      }
    }
    string last(first.rbegin(), first.rend());
    if (odd == 1)
      first.push_back(c);
    first += last;
    if (first <= target)
      return "";
    string ans(n, ' ');
    if (odd == 1) {
      ans[n / 2] = c;
      --cnt[c - 'a'];
    }
    for (int i = 0; i < n / 2; ++i) {
      if (cnt[target[i] - 'a'] >= 2) {
        ans[i] = target[i];
        cnt[target[i] - 'a'] -= 2;
      } else {
        bool found = false;
        while (!found) {
          for (int j = target[i] - 'a' + 1; j < 26; ++j) {
            if (cnt[j] >= 2) {
              ans[i] = 'a' + j;
              cnt[j] -= 2;
              found = true;
              break;
            }
          }
          if (!found) {
            --i;
            cnt[ans[i] - 'a'] += 2;
          }
        }
        for (size_t k = i + 1; k < n / 2; ++k) {
          for (int j = 0; j < 26; ++j) {
            if (cnt[j] >= 2) {
              ans[k] = 'a' + j;
              cnt[j] -= 2;
              break;
            }
          }
        }
        for (int i = 0; i < n / 2; ++i) {
          ans[n - 1 - i] = ans[i];
        }
        return ans;
      }
    }
    for (int i = 0; i < n / 2; ++i) {
      ans[n - 1 - i] = ans[i];
    }
    if (ans > target)
      return ans;
    int k = n / 2 - 1;
    cnt[ans[k] - 'a'] += 2;
    for (int i = k - 1; i >= 0; --i) {
      bool found = false;
      for (int j = ans[i] - 'a' + 1; j < 26; ++j) {
        if (cnt[j] >= 2) {
          cnt[ans[i] - 'a'] += 2;
          ans[i] = 'a' + j;
          cnt[j] -= 2;
          found = true;
          break;
        }
      }
      if (found) {
        for (int kk = i + 1; kk < n / 2; ++kk) {
          for (int j = 0; j < 26; ++j) {
            if (cnt[j] >= 2) {
              ans[kk] = 'a' + j;
              cnt[j] -= 2;
              break;
            }
          }
        }
        for (int i = 0; i < n / 2; ++i) {
          ans[n - 1 - i] = ans[i];
        }
        return ans;
      } else {
        cnt[ans[i] - 'a'] += 2;
      }
    }

    return ans;
  }
};
