#include <signal.h>
void setup_handlers() { signal(SIGINT, SIG_IGN); }
