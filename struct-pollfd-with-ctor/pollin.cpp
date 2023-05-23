#include <iostream>
#include <string>
#include <vector>

#include <sys/poll.h>

using namespace std;

struct pollin : public pollfd {
    pollin(int infd) {
        fd = infd;
        events = POLLIN;
    }
};

int main() {
    vector<pollin> pollins;
    pollins.emplace_back(0);
    pollins.emplace_back(1);
    pollins.emplace_back(2);
    int status = poll(pollins.data(), pollins.size(), 0);
    cout << status << endl;


    // POD default ctor zeroes fields, unlike malloc
    vector<struct pollfd> pollfds;
    for (int i = 0; i < 3; i++ ) {
        pollfds.emplace_back();
        auto pollfd = pollfds.back();
        cout << pollfd.fd << '\t' << pollfd.events << '\t' << pollfd.revents << endl;
    }
}