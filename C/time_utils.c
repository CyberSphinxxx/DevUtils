#include <time.h>
void print_time() { time_t t = time(NULL); printf("%s", ctime(&t)); }
