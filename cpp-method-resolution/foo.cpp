#include <iostream>
#include <sys/socket.h>

using namespace std;

void send(int foo, int bar, int quux, int thud) {
    cout << foo << bar << quux << thud << endl;
}

int main() {
    send(1, 2, 3, 4);
    return 0;
}
