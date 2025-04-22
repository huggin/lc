const int MOD = 1e9 + 7;
const int MAX = 10005;

// Precompute factorials and inverse factorials for combinatorial calculations
vector<long long> fact(MAX), invFact(MAX);

// Fast exponentiation
long long modPow(long long a, long long b, long long mod) {
    long long res = 1;
    a %= mod;
    while (b > 0) {
        if (b & 1) res = res * a % mod;
        a = a * a % mod;
        b >>= 1;
    }
    return res;
}

// Initialize factorials and inverse factorials
void initFactorials(int n) {
    fact[0] = invFact[0] = 1;
    for (int i = 1; i <= n; i++) {
        fact[i] = fact[i - 1] * i % MOD;
    }
    invFact[n] = modPow(fact[n], MOD - 2, MOD);
    for (int i = n - 1; i >= 1; i--) {
        invFact[i] = invFact[i + 1] * (i + 1) % MOD;
    }
}

// Combination function
long long comb(int n, int k) {
    if (k < 0 || k > n) return 0;
    return fact[n] * invFact[k] % MOD * invFact[n - k] % MOD;
}

class Solution {
public:
    int idealArrays(int n, int maxValue) {
        initFactorials(n + 4);  // Precompute enough factorials

        vector<unordered_map<int, long long>> dp(n + 1);
        for (int i = 1; i <= maxValue; i++) {
            dp[1][i] = 1;
        }

        for (int i = 2; i <= n; i++) {
            for (auto& [k, v] : dp[i - 1]) {
                for (int j = 2; j * k <= maxValue; j++) {
                    dp[i][j * k] = (dp[i][j * k] + v) % MOD;
                }
            }
        }

        long long ans = 0;
        for (int i = 1; i <= n; i++) {
            long long total = 0;
            for (auto& [key, value] : dp[i]) {
                total = (total + value) % MOD;
            }
            ans = (ans + total * comb(n - 1, i - 1) % MOD) % MOD;
        }
        return ans;
    }
};
