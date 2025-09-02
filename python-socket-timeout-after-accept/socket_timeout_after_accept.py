from socket import socket, SHUT_RDWR
from socketserver import TCPServer, BaseRequestHandler
from threading import Thread
from time import sleep

class ImpatientRequestHandler(BaseRequestHandler):
    def setup(self):
        self.request.settimeout(1)

    def handle(self):
        data = self.request.recv(1024)
        print(f"received {data}")

def main():
    svr = TCPServer(("0.0.0.0", 8000), ImpatientRequestHandler)
    svr_thread = Thread(target=svr.serve_forever)
    svr_thread.start()

    sock = socket()
    try:
        sock.connect(("localhost", 8000))
        sock.sendall(b"hello!")
        sleep(2)
    finally:
        sock.shutdown(SHUT_RDWR)
        sock.close()
        svr.shutdown()
        svr.server_close()

if __name__ == "__main__":
    main()