#include<iostream>
using namespace std;

class Node{
    public:
        int data;
        Node* next;
};

void printList(Node* node)
{
    while (node != NULL)
    {
        cout << node->data << " ";
        node = node->next;
    }
    cout<<endl;
}
 

void push(Node** head_ref, int new_data){
    Node* new_node = new Node();
    new_node->data = new_data;
    new_node->next = *head_ref;
    *head_ref = new_node; 
}

void deleteNode(Node** head_ref, int delete_node){
    Node* temp = *head_ref;
    Node* prev = NULL;

    if (temp != NULL && temp->data == delete_node){
        *head_ref = temp->next;
        delete temp;
        return;
    }

    while (temp != NULL && temp->data != delete_node){
        prev = temp;
        temp = temp->next;
    }
    if (temp == NULL){
        return;
    }
    prev->next = temp->next;
    delete temp;
}

int main(){
    Node* head = NULL;
    push(&head, 2);
    push(&head, 4);
    push(&head, 6);
    push(&head, 1);
    printList(head);

    deleteNode(&head, 6);
    printList(head);
    
    
    return 0;
}