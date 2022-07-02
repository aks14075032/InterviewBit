/**
#Problem -- https://www.interviewbit.com/problems/reverse-alternate-k-nodes/
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
ListNode* reverse(ListNode* head, int B){
    if (!head) return NULL;
    ListNode* curr = head, *prev = NULL, *nextP = NULL;
    int count = 0;
    while(curr != NULL && count < B){
        nextP = curr->next;
        curr->next = prev;
        prev = curr;
        curr = nextP;
        count += 1;
    }
    // cout<<head->val<<" "<<nextP->val<<" "<<curr->val<<endl;
    if (head != NULL)
        head->next = curr;
    count = 0;
    while(curr != NULL && count < B-1){
        curr = curr->next;
        count += 1;
    }
    if (curr != NULL)
        curr->next = reverse(curr->next, B);
    return prev;
    
}
ListNode* Solution::solve(ListNode* A, int B) {
    return reverse(A, B);
}
