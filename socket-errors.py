# Handling socket errors gracefully

'''In any networking application, it is very common that one end is trying to connect, but the
other party is not responding due to networking media failure or any other reason. The
Python socket library has an elegant method of handing these errors via the
socket.error exceptions. In this recipe, a few examples are presented.'''

# Use examine this code use the below command

'''$ python3 <YOUR_FILE_NAME>.py --host=<HOST> --port=<PORT> --file=<FILE>'''

import sys
import socket
import argparse

def main():
    # setup argument parsing
    parser = argparse.ArgumentParser(description='Socket Error Examples')
    parser.add_argument('--host',action="store",dest="host",required=False)
    parser.add_argument('--port',action="store",dest="port",type=int,required=False)
    parser.add_argument('--file',action="store",dest="file",required=False)

    give_args = parser.parse_args()
    host = give_args.host
    port = give_args.port
    filename = give_args.file

    # First try-except block -- create socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as e:
        print("Error creating socket: %s" %e)
        sys.exit(1)

    # Second try-except block -- connect to a given host/port
    try:
        s.connect((host,port))
    except socket.gaierror as e:
        print("Connection error: %s" %e)
        sys.exit(1)

    # Third try-except block -- sending data
    try:
        msg = "GET %s HTTP/1.0\r\n\r\n" %filename
        s.sendall(msg.encode('utf-8'))
    except socket.error as e:
        print("Error sending data: %s" %e)
        sys.exit(1)
    
    while 1:
        # Fourth try-except block --waiting
        try:
            buf = s.recv(2048)
        except socket.error as e:
            print("Error receiving data: %s" % e)
            sys.exit(1)
        if not len(buf):
            break

        # Write the receive data
        sys.stdout.write(buf.decode('utf-8'))

if __name__ == "__main__":
    main()