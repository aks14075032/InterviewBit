/**
  #Problem -- https://www.interviewbit.com/problems/remove-duplicates-from-sorted-list/
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
ListNode* Solution::deleteDuplicates(ListNode* A) {
    ListNode* temp = A;
    ListNode* prev = A;
    ListNode* curr = A;
    ListNode* new_head = prev;
    while (temp != NULL){
        if (prev->val != temp->val){
            prev->next = temp;
            prev = temp;
        }
        else if(temp->next == NULL){
            prev->next = NULL;
        }
        temp = temp->next;
    }
    return new_head;
}
