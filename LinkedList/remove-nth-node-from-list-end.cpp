/**
 #Problem -- https://www.interviewbit.com/problems/remove-nth-node-from-list-end/
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
ListNode* Solution::removeNthFromEnd(ListNode* A, int B) {
    if (!A){
        return A;
    }
    ListNode* temp = A;
    int count = 0;
    while(temp != NULL){
        count += 1;
        temp = temp->next;
    }
    int z = count-B;
    
    if (z <= 0){
        A = A->next;
        return A; 
    }
    ListNode* curr = A, *prev = NULL;
    while(z > 0){
        z -= 1;
        prev = curr;
        curr = curr->next;
    }
    prev->next = curr->next;
    return A;
    
}   
