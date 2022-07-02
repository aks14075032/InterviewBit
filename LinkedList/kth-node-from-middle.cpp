/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */


int Solution::solve(ListNode* A, int B) {
    ListNode* slow_ptr = A, *fast_ptr = A->next;
    int count = 0;
    while (fast_ptr != NULL && fast_ptr->next != NULL){
        slow_ptr = slow_ptr->next;
        count += 1;
        fast_ptr = fast_ptr->next->next;
    }
    ListNode* midNode = slow_ptr;
    if (fast_ptr != NULL){
        midNode = slow_ptr->next;
        count += 1;
    }
    int z = count - B;
    if (z < 0){
        return -1;
    }
    ListNode* temp = A;
    while (z > 0){
        z -= 1;
        temp = temp->next;
    }
    return temp->val;
    
}
