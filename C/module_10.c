#include <stdlib.h>

int* allocate_10() {
    return (int*)malloc(sizeof(int) * 10);
}
