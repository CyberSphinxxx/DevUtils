#define MAX 100
int queue[MAX]; int f = -1, r = -1;
void enqueue(int x) { if(r < MAX-1) queue[++r] = x; }
