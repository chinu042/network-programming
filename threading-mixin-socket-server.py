# Using ThreadingMixIn in your socket server applications

'''Perhaps you prefer writing a multi-threaded application over a process-based one due to
any particular reason, for example, sharing the states of that application across threads,
avoiding the complexity of inter-process communication, or something else. In such a
situation, if you want to write an asynchronous network server using SocketServer
library, you will need ThreadingMixIn.'''

import os
import socket
import threading
import socketserver

SERVER_HOST = 'localhost'
SERVER_PORT = 0  # tells the kernel to pickup a port dynamically
BUF_SIZE = 1024

def client(ip, port, message):

    """ A client to test threading mixin server"""
    # Connect to the server
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    try:
        sock.sendall(bytes(message, 'utf-8'))
        response = sock.recv(BUF_SIZE)
        print("Client received: %s" % response)
    finally:
        sock.close()

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):

    """ An example of threaded TCP request handler """
    def handle(self):
        data = self.request.recv(1024)
        cur_thread = threading.current_thread()
        response = "%s: %s" % (cur_thread.name, data)
        self.request.sendall(bytes(response, 'utf-8'))

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    """Nothing to add here, inherited everything necessary from parents"""
    pass

if __name__ == "__main__":
    # Run server
    server = ThreadedTCPServer((SERVER_HOST, SERVER_PORT), ThreadedTCPRequestHandler)
    ip, port = server.server_address  # retrieve ip address

    # Start a thread with the server -- one thread per request
    server_thread = threading.Thread(target=server.serve_forever)
    
    # Exit the server thread when the main thread exits
    server_thread.daemon = True
    server_thread.start()
    print("Server loop running on thread: %s" % server_thread.name)

    # Run clients
    client(ip, port, "Hello from client 1")
    client(ip, port, "Hello from client 2")
    client(ip, port, "Hello from client 3")

    # Server cleanup
    server.shutdown()

'''This recipe first creates a server thread and launches it in the background. Then it launches
three test clients to send messages to the server. In response, the server echoes back the
message to the clients. In the handle() method of the server's request handler, you can see
that we retrieve the current thread information and print it. This should be different in each
client connection.
In this client/server conversation, the sendall() method has been used to guarantee the
sending of all data without any loss:'''