#include <iostream>
#include <vector>

using namespace std;

class VectorMover {
    public:
      vector<unsigned char> data;
      VectorMover(vector<unsigned char> &&other) : data(other) {}
};

int main() {
    auto data = vector<unsigned char>({0x01, 0x02, 0x03, 0x04, 0x05, 0x06});
    auto vm = VectorMover(move(data));
    cout << "data size: " << data.size() << " and vm size " << vm.data.size() << endl;
}