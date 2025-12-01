#define MAX 100
int stack[MAX]; int top = -1;
void push(int x) { if(top < MAX-1) stack[++top] = x; }
int pop() { return (top >= 0) ? stack[top--] : -1; }
