#include <stdio.h>

void json_start_obj(char* buf) { sprintf(buf, "{"); }
void json_end_obj(char* buf) { sprintf(buf, "}"); }
