/**
 * Problem -- https://www.interviewbit.com/problems/sort-binary-linked-list/   
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
ListNode* Solution::solve(ListNode* A) {
    ListNode* temp = A;
    ListNode* curr = A;

    while (temp != NULL){
        if (temp->val == 0 && curr->val == 1){
            temp->val = 1;
            curr->val = 0;
        }
        temp = temp->next;
        if (curr->val != 1) curr = curr->next;
    }
    return A;
}
