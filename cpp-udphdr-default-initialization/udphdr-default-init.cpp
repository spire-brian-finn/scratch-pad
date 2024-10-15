#include <iostream>
#include <linux/udp.h>

using namespace std;
int main() {
    udphdr hdr = udphdr();
    cout << "src " << hdr.source << " dest " << hdr.dest << " len " << hdr.len << " checksum " << hdr.check << endl << flush;
}