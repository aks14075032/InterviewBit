/**
Problem -- https://www.interviewbit.com/problems/reorder-list/
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
ListNode* Solution::reorderList(ListNode* A) {
    vector<int> ele;
    ListNode* temp = A;
    while(temp != NULL){
        ele.push_back(temp->val);
        temp = temp->next;
    }
    int i = 0, j=ele.size()-1;
    temp = A;
    while(temp != NULL){
        temp->val = ele[i++];
        temp = temp->next;
        if (temp == NULL) break;
        temp->val = ele[j--];
        temp = temp->next;
    }
    return A;
}
