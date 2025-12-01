#include <stdio.h>

int file_exists(const char* filename) {
    FILE* f = fopen(filename, "r");
    if (f) { fclose(f); return 1; }
    return 0;
}
