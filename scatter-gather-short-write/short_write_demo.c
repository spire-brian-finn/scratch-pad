#include <stdio.h>
#include <sys/uio.h>

int buf[5] = {1, 2, 3, 4, 5};
int buf2[4] = {6, 7, 8, 9};

struct iovec iovecs[2] = {
    {.iov_base = buf, .iov_len=5},
    {.iov_base = buf2, .iov_len=4}
};

int main() {
    int num_buffers = 2;
    struct iovec* start = iovecs;
    int offset = 0;
    printf("%d buffers; start %p: %zu\n", num_buffers, start, start->iov_len);

    while (offset > 0) {
        if (offset < start->iov_len) {
            start->iov_base += offset;
            start->iov_len -= offset;
            break;
        } else {
            offset -= start->iov_len;
            ++start;
            --num_buffers;
        }
    }
    printf("%d buffers; start %p: %zu\n", num_buffers, start, start->iov_len);
}