#Finding a service name, given the port and protocol

'''If you would like to discover network services, it may be helpful to determine what
network services run on which ports using either the TCP or UDP protocol.'''

'''If you know the port number of a network service, you can find the service name using the
getservbyport() socket class function from the socket library. You can optionally give
the protocol name when calling this function.'''

import socket

def find_service_name():
    protocolname = 'tcp'
    for port in [443,80,25]:
        print("Port: %s => service name: %s" %(port, socket.getservbyport(port,protocolname)))
    print("Port: %s => service name: %s" %(53,socket.getservbyport(53,'udp')))

if __name__ == "__main__":
    find_service_name()