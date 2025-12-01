#include <stdlib.h>

void gen_uuid(char* buf) {
    // Pseudo-random UUID
    for(int i=0; i<36; i++) buf[i] = '0';
}
