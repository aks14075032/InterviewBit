/**
#Problem -- https://www.interviewbit.com/problems/insertion-sort-list/
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */


ListNode* Solution::insertionSortList(ListNode* A) { 
    if(!A || !A->next)
        return A;
        
    ListNode* temp = A;
    ListNode* sorted = NULL;
    
    while(temp != NULL){
        ListNode* curr = temp;
        temp = temp->next;
        if(sorted == NULL || sorted->val >= curr->val){
            curr->next = sorted;
            sorted = curr;
        }
        else{
            ListNode* temp1 = sorted;
            while (temp1)
            {
                ListNode* s = temp1;
                temp1 = temp1->next;
                
                if (!s->next || s->next->val > curr->val)
                {
                    curr->next = s->next;
                    s->next = curr;
                    break;
                }
            }
        }
    }
    return sorted;
}
