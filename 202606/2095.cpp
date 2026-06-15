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
  ListNode *deleteMiddle(ListNode *head) {
    int n = 0;
    auto p = head;
    while (p) {
      ++n;
      p = p->next;
    }
    if (n == 1)
      return nullptr;
    p = head;
    for (int i = 0; i < n / 2 - 1; ++i) {
      p = p->next;
    }
    auto q = p->next;
    p->next = q->next;
    return head;
  }
};
