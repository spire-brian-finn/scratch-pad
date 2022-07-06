#include <errno.h>
#include <fcntl.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>

int main() {
    int fd = open("/tmp/", __O_TMPFILE | O_RDWR);
    printf("Starting fd: %d\n", fd);
    int dup_fd = dup(fd);
    printf("Duplicate fd: %d\n", dup_fd);

    int ret = close(fd);
    printf("Closing original fd returned %d\n", ret);
    ret = write(fd, "foo", 3);
    printf("Writing to closed original fd returned %d\n", ret);
    if (ret < 0) {
        printf("Errno %d: %s\n", errno, strerror(errno));
    }

    ret = write(dup_fd, "bar", 3);
    printf("Writing to open dup fd after closing original returned %d\n", ret);
    if (ret < 0) {
        printf("Errno %d: %s\n", errno, strerror(errno));
    }

    ret = close(dup_fd);
    printf("Closing duplicate fd returned %d\n", ret);
    if (ret < 0) {
        printf("Errno %d: %s\n", errno, strerror(errno));
    }
}