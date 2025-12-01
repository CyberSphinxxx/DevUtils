#include <string.h>

const char* get_ext(const char* path) {
    const char* dot = strrchr(path, '.');
    return (!dot || dot == path) ? "" : dot + 1;
}
