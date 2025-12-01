#include <stdlib.h>

int* allocate_2() {
    return (int*)malloc(sizeof(int) * 2);
}
