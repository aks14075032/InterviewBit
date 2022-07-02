/**
#Problem -- https://www.interviewbit.com/problems/k-reverse-linked-list/
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

ListNode* reverse(ListNode* head, int B){
    if (!head){
        return NULL;
    }
    ListNode* temp = head;
    ListNode* nextP = NULL;
    ListNode* prev = NULL;
    int count = 0;
    
    while(temp != NULL && count < B){
        nextP = temp->next;
        temp->next = prev;
        prev = temp;
        temp = nextP;
        count += 1;
    }
    if (nextP != NULL){
        head->next = reverse(nextP, B);
    }
    
    return prev;
}

ListNode* Solution::reverseList(ListNode* A, int B) {
    if (B == 1 || !A || !A->next){
        return A;
    }
    ListNode* ans = reverse(A, B);
    return ans;
}
