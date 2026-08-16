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
    ListNode* removeElements(ListNode* head, int val) {
        ListNode dummy(-1, head);
        ListNode * prev = &dummy;
        ListNode * curr = head;

        while (curr) {
            ListNode * nxt = curr->next;
            if (curr->val == val) {
                prev->next = nxt;
            } else {
                prev = curr;
            }
            curr = nxt;
        }

        return dummy.next;
    }
};
