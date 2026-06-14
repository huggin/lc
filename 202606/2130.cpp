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
  int pairSum(ListNode *head) {
    vector<int> vals;
    ListNode *p = head;
    while (p) {
      vals.push_back(p->val);
      p = p->next;
    }
    int ans = 0;
    int n = vals.size();
    for (int i = 0; i < n / 2; ++i) {
      ans = max(ans, vals[i] + vals[n - 1 - i]);
    }
    return ans;
  }
};
