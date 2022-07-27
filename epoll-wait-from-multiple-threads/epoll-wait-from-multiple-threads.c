#include <fcntl.h>
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/epoll.h>
#include <sys/socket.h>
#include <sys/un.h>

struct thread_info {
    int epoll_fd;
    int thread_id;
};

void* wait_on_epoll(void* args) {
    struct thread_info* tinfo = (struct thread_info *) args;
    struct epoll_event events[2] = {0};
    epoll_wait(tinfo->epoll_fd, events, 2, -1);
    printf("oH gOoDy %d\n", tinfo->thread_id);
}

int main() {
    int server = socket(AF_UNIX, SOCK_DGRAM, 0);
    struct sockaddr_un name = {
        .sun_family = AF_UNIX,
        .sun_path = "sock"
    };
    bind(server, (struct sockaddr *) &name, sizeof(struct sockaddr_un));

    int epoll_fd = epoll_create1(0);
    struct epoll_event event = {
        .data.fd = server,
        .events = EPOLLIN | EPOLLOUT
    };
    epoll_ctl(epoll_fd, EPOLL_CTL_ADD, server, &event);
    struct thread_info args[10];
    pthread_t threads[10];
    for (int i = 0; i < 10; ++i) {
        args[i].epoll_fd = epoll_fd;
        args[i].thread_id = i;
        pthread_create(threads, NULL, wait_on_epoll, &args[i]);
    }

    int client = socket(AF_UNIX, SOCK_DGRAM, 0);
    sendto(client, "foo", 4, 0, (struct sockaddr*) &name, sizeof(struct sockaddr_un));


    for (int i = 0; i < 10; ++i) {
        pthread_join(threads[i], NULL);
    }
}




/*
epollet - what happens if the edge happens when you aren't in epoll_wait?
i.e.
epoll_wait()
while not eagain {
    read()
}
sleep(a while) <- send the socket some new data here
epoll_wait() <- do I get woken up, or has the edge passed? If the latter, and rx queue is full, I will deadlock
*/