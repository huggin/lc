class Solution {
public:
  long long minimumCost(vector<int> &nums, int k, int dist) {
    multiset<int> used;
    multiset<int> aval;
    int n = nums.size();
    long long curr = 0;
    for (int i = 1; i < k; i++) {
      used.insert(nums[i]);
      curr += nums[i];
    }
    long long ans = curr;

    for (int i = k; i < n; i++) {
      int j = i - dist - 1;
      if (j >= 1) {
        if (used.find(nums[j]) != used.end()) {
          used.erase(used.find(nums[j]));
          curr -= nums[j];
        } else {
          aval.erase(aval.find(nums[j]));
        }
      }
      aval.insert(nums[i]);
      if (used.size() < k - 1) {
        auto it = aval.begin();
        curr += *it;
        used.insert(*it);
        aval.erase(it);
      }
      if (*aval.begin() < *used.rbegin()) {
        auto it = used.end();
        --it;
        curr -= *it;
        aval.insert(*it);
        used.erase(it);
        curr += *aval.begin();
        used.insert(*aval.begin());
        aval.erase(aval.begin());
      }
      ans = min(ans, curr);
    }

    return ans + nums[0];
  }
};
