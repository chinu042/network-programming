# Changing a socket to the blocking/non-blocking mode

'''By default, TCP sockets are placed in a blocking mode. This means the control is not
returned to your program until some specific operation is complete. If you call the
connect() API, the connection blocks your program until the operation is complete. On
many occasions, you don't want to keep your program waiting forever, either for a response
from the server or for any error to stop the operation. For example, when you write a web
browser client that connects to a web server, you should consider a stop functionality that
can cancel the connection process in the middle of this operation. This can be achieved by
placing the socket in the non-blocking mode.'''

import socket

def test_socket_modes():

    #Create a TCP socket:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

    # Set the socket to blocking mode using setblocking(1). In blocking mode, 
    # operations like accept() and recv() will block until they complete:
    s.setblocking(1)

    # Set a timeout of 0.5 seconds for socket operations using settimeout(0.5). 
    # This means that socket operations will raise a timeout exception if they take longer than 0.5 seconds:
    s.settimeout(0.5)

    # Bind the socket to a local address and port. In this case, 
    # it binds to localhost (127.0.0.1) and a port chosen by the system (0 indicates any available port):
    s.bind(("127.0.0.1", 0))

    # Get the socket's local address and port using getsockname():
    socket_address = s.getsockname()
    print ("Trivial Server launched on socket: %s" %str(socket_address))
    while(1):
        s.listen(1)

if __name__ == '__main__':
    test_socket_modes()