#include <string.h>
#include <ctype.h>

void to_upper(char* str) {
    for(int i=0; str[i]; i++) str[i] = toupper(str[i]);
}

void to_lower(char* str) {
    for(int i=0; str[i]; i++) str[i] = tolower(str[i]);
}
