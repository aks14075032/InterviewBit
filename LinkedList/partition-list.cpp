/**
 * Problem -- https://www.interviewbit.com/problems/partition-list/
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

ListNode* Solution::partition(ListNode* A, int B) {
    ListNode* lessThan = NULL, *lessThanHead = NULL;
    ListNode* equalTo = NULL, *equalToHead = NULL;
    ListNode* greaterThan = NULL, *greaterThanHead = NULL;
    
    ListNode* temp = A;
    while (temp != NULL){
        if (temp->val < B){
            if (lessThanHead == NULL){
                lessThan=lessThanHead = temp;
            }
            else{
                lessThan->next = temp;
                lessThan = lessThan -> next;
            }
        }
        else{
            if (greaterThanHead == NULL){
                greaterThan=greaterThanHead = temp;
            }
            else{
                greaterThan->next = temp;
                greaterThan = greaterThan -> next;
            }
        }
        temp = temp->next;
    }
    if (greaterThan != NULL) greaterThan->next = NULL;
    
    if (lessThanHead == NULL){
        return greaterThanHead;
    }
    
    
    lessThan->next = greaterThanHead;
    return lessThanHead;
}
