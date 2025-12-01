#include <stdlib.h>

void* pool_alloc(size_t size) { return malloc(size); }
void pool_free(void* ptr) { free(ptr); }
