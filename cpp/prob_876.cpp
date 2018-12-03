/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* middleNode(ListNode* head) {
        ListNode* curr_node = head;
        ListNode* curr_middle_node = head;
        int curr_middle_count = 1;
        
        while (curr_node -> next) {
            curr_node = curr_node -> next;
            curr_middle_count++;
            if (curr_middle_count % 2 == 0) {
                curr_middle_node = curr_middle_node -> next;
            };
        };
        return curr_middle_node;
    };
};