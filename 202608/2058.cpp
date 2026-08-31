/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
  vector<int> nodesBetweenCriticalPoints(ListNode *head) {
    int curr = 0;
    vector<int> cps;
    ListNode *p = head;
    while (p && p->next && p->next->next) {
      if (p->val < p->next->val && p->next->val > p->next->next->val ||
          p->val > p->next->val && p->next->val < p->next->next->val) {
        cps.push_back(curr);
      }
      ++curr;
      p = p->next;
    }
    vector<int> ans{-1, -1};
    if (cps.size() < 2)
      return ans;
    ans[1] = cps[cps.size() - 1] - cps[0];
    ans[0] = INT_MAX;
    for (int i = 1; i < cps.size(); ++i) {
      ans[0] = min(ans[0], cps[i] - cps[i - 1]);
    }
    return ans;
  }
};
