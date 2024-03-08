import socket
import struct
import sys
import time

NTP_SERVER = "0.uk.pool.ntp.org"
TIME1970 = 2208988800

def sntp_client():
    """
    Simple SNTP client that queries an NTP server and prints the time.
    """
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = b'\x1b' + b'\0' * 47
    client.sendto(data, (NTP_SERVER, 123))
    data, address = client.recvfrom(1024)

    if data:
        print('Response received from:', address.decode())
    t = struct.unpack('!12I', data)[10]
    t -= TIME1970
    print('\tTime=%s' % time.ctime(t))

if __name__ == '__main__':
    sntp_client()
