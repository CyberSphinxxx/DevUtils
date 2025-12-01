#include <stdio.h>
void print_hex(unsigned char* data, int len) {
    for(int i=0; i<len; i++) printf("%02x ", data[i]);
    printf("\n");
}
