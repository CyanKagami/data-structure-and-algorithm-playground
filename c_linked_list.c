#include <stdio.h>
#include <stdlib.h>
struct node
{
    int val;
    struct node* next;
};

struct node* createNode(int val){
    struct node* newNode = (struct node*)malloc(sizeof(struct node));
    newNode->val = val;
    newNode->next = NULL;
    return newNode;
}

int main(){
    int arr[5] = {1,2,3,4,5};
    struct node* head = NULL;
    struct node* current = head;
    for(int i=0;i<5;i++){
        if (head == NULL){
            head = createNode(arr[i]);
            current = head;
        }
        else{
            current->next = createNode(arr[i]);
            current = current->next;
        }
    }
    current = head;
    struct node* clean;
    while (current!=NULL){
        printf("%d\n",current->val);
        clean = current;
        current = current->next;
        free(clean);
        printf("%d\n\n",clean->val);
    }
    return 0;
}