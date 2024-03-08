# Reusing socket addresses

'''This code sets up a TCP server that listens on a specified port for incoming connections. 
It demonstrates the use of the `SO_REUSEADDR` socket option to allow the server to quickly reuse the same address for subsequent connections, 
even if the socket has been closed recently.'''

import socket
import sys

def reuse_socket_addr():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Get the old state of the SO_REUSEADDR option
    old_state = sock.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
    print("Old socket state: %s" %old_state)

    # Enable the SO_REUSEADDR option
    sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    new_state = sock.getsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR)
    print("New socket state: %s" %new_state)

    local_port = 8282
    srv = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

    srv.bind( ('',local_port) )
    srv.listen(1)
    print("Listening on port: %s" %local_port)

    while True:
        try:
            connection, addr = srv.accept()
            print("Connected by %s: %s" %(addr[0],addr[1]))
        except KeyboardInterrupt:
            break
        except socket.error as msg:
            print("%s" %(msg,))

if __name__ == "__main__":
    reuse_socket_addr()
