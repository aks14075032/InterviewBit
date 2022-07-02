/**
 #Problem -- https://www.interviewbit.com/problems/sort-list/
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

ListNode* sortedMerge(ListNode* a, ListNode* b){
    ListNode* result = NULL;
    
    if (a == NULL){
        return b;
    }
    if (b == NULL){
        return a;
    }
    if (a->val <= b->val){
        result = a;
        result->next = sortedMerge(a->next, b);
    }
    else{
        result = b;
        result->next = sortedMerge(a, b->next);
    }
    return result;
}

void SplitIntoTwo(ListNode* source, ListNode** a, ListNode** b){
    ListNode* fast_ptr = source->next, *slow_ptr = source;
    
    while (fast_ptr != NULL && fast_ptr->next != NULL){
        slow_ptr = slow_ptr->next;
        fast_ptr = fast_ptr->next->next;
    }
    
    *a = source;
    *b = slow_ptr->next;
    slow_ptr->next = NULL;
    
}

void MergeSort(ListNode** head_ref){
    ListNode* head = *head_ref;
    ListNode* a, *b;
    
    if (head == NULL || head->next == NULL){
        return;
    }
    SplitIntoTwo(head, &a, &b);
    MergeSort(&a);
    MergeSort(&b);
    
    *head_ref = sortedMerge(a, b);
} 

ListNode* Solution::sortList(ListNode* A) {
    MergeSort(&A);
    return A;
}
