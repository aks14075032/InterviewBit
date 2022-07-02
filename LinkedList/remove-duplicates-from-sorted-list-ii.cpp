/**
#Problem -- https://www.interviewbit.com/problems/remove-duplicates-from-sorted-list-ii/
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
ListNode* Solution::deleteDuplicates(ListNode* A) {
    if (!A || !A->next){
        return A;
    }
    ListNode* new_head = NULL;
    ListNode* curr = A;
    ListNode* prev = NULL;
    ListNode* nextP = A->next;
    while(nextP != NULL){
        if (curr->val != nextP->val){
            
            // cout<<curr->val<<" "<<nextP->val<<endl;
            if (curr->next == nextP){
                if (prev == NULL){
                    prev = curr;
                    new_head = prev;
                }
                else{
                    prev->next = curr;
                    prev = curr;
                }
            }
            else if(prev != NULL){
                prev->next = nextP;
            }
            curr = nextP;
        }
        else if(nextP->next == NULL){
            if (prev != NULL)
                prev->next = NULL;
        }
        nextP = nextP->next;
    }
    return new_head;
}
