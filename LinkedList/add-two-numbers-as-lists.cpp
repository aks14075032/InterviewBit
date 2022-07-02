/**
#Problem -- https://www.interviewbit.com/problems/add-two-numbers-as-lists/
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

ListNode* reverse(ListNode* head){
    ListNode* curr = head, *prev=NULL, *nextP = NULL;
    while(curr != NULL){
        nextP = curr->next;
        curr->next = prev;
        prev = curr;
        curr = nextP;
    }
    return prev;
}

ListNode* Solution::addTwoNumbers(ListNode* A, ListNode* B) {
    if (!A) return B;
    if (!B) return A;
    ListNode* A_rev = A;
    ListNode* B_rev = B;
    
    ListNode* result = NULL;
    ListNode* result_head = NULL;
    int carry = 0;
    while (A_rev != NULL && B_rev != NULL){
        int curr = A_rev->val + B_rev->val+carry;
        // cout<<A_rev->val<<" "<<B_rev->val<<endl;
        if (curr >= 10){
            carry = 1;
        }
        else{
            carry = 0;
        }
        ListNode* new_node = new ListNode(curr%10);
        if(result == NULL){
            result = new_node;
            result_head = result;
        }
        else{
            result->next = new_node;
            result = new_node;
        }
        A_rev = A_rev->next;
        B_rev = B_rev->next;
    }
    
    while (A_rev != NULL){
        int curr = A_rev->val+carry;
        if (curr >= 10){
            carry = 1;
        }
        else{
            carry = 0;
        }
        ListNode* new_node = new ListNode(curr%10);
        result->next = new_node;
        result = new_node;
        A_rev = A_rev->next;
    }
    while (B_rev != NULL){
        int curr = B_rev->val+carry;
        if (curr >= 10){
            carry = 1;
        }
        else{
            carry = 0;
        }
        ListNode* new_node = new ListNode(curr%10);
        result->next = new_node;
        result = new_node;
        B_rev = B_rev->next;
    }
    if (carry){
        ListNode* new_node = new ListNode(1);
        result->next = new_node;
        result = new_node;
    }
    result->next = NULL;
    // ListNode* ans = reverse(result_head);
    return result_head;
    
}
