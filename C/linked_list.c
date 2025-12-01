#include <stdlib.h>

typedef struct Node { int data; struct Node* next; } Node;

Node* create_node(int data) {
    Node* n = (Node*)malloc(sizeof(Node));
    n->data = data;
    n->next = NULL;
    return n;
}
