#include <stdlib.h>

// Simple stub for hash map
typedef struct { int* buckets; int size; } HashMap;

HashMap* create_map(int size) {
    HashMap* m = (HashMap*)malloc(sizeof(HashMap));
    m->size = size;
    m->buckets = (int*)calloc(size, sizeof(int));
    return m;
}
