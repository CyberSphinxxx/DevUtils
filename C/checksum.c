unsigned int checksum(const char* data) {
    unsigned int sum = 0;
    while(*data) sum += *data++;
    return sum;
}
