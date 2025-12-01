#include <string.h>

void parse_csv_line(char* line) {
    char* token = strtok(line, ",");
    while(token) { token = strtok(NULL, ","); }
}
