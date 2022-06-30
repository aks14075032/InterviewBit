/**
  #Problem -- https://www.interviewbit.com/problems/palindrome-list/
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

bool compare_list(ListNode* head1, ListNode* head2){
    ListNode* temp1 = head1;
    ListNode* temp2 = head2;
    
    while (temp1 && temp2){
        if(temp1->val != temp2->val){
            return false;
        }
        temp1 = temp1->next;
        temp2 = temp2->next;
    }
    if (temp1 == NULL && temp2 == NULL){
        return true;
    }
    return false;
}

 void reverse(ListNode** head){
     ListNode* prev = NULL, *nextP = NULL, *curr= *head;
     
     while (curr != NULL){
        nextP = curr->next;
        curr->next = prev;
        prev = curr;
        curr = nextP;
    }
    *head = prev;   
 }
 
int Solution::lPalin(ListNode* A) {
    if (A->next == NULL) return 1;
    ListNode* slow_ptr_prev = A, *midnode = NULL; 
    ListNode* slow_ptr = A, *fast_ptr = A;
    ListNode* second_half;
    
    while (fast_ptr != NULL && fast_ptr->next != NULL){
        fast_ptr = fast_ptr->next->next;
        slow_ptr_prev = slow_ptr;
        slow_ptr = slow_ptr->next;
    }
    
    if (fast_ptr != NULL){
        midnode = slow_ptr;
        slow_ptr = slow_ptr->next;
    }
    
    second_half = slow_ptr;
    slow_ptr_prev->next = NULL;
    
    reverse(&second_half);
    
    bool res = compare_list(A, second_half);
    
    reverse(&second_half);
    
    if (midnode != NULL){
        slow_ptr_prev->next = midnode;
        midnode->next = second_half;
    }
    else{
        slow_ptr_prev->next = second_half;
    }
    return res;
}
