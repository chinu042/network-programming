# Writing an SNTP client

'''Sometimes, you don't need to get the precise time from the NTP
server. You can use a simpler version of NTP called simple network time protocol.'''

'''This SNTP client creates a socket connection and sends the protocol data. After receiving
the response from the NTP server (in this case, 0.uk.pool.ntp.org), it unpacks the data
with struct. Finally, it subtracts the reference time, which is January 1, 1970, and prints the
time using the ctime() built-in method in the Python time module.'''

import socket
import struct
import sys
import time

NTP_SERVER = "0.uk.pool.ntp.org"
TIME1970 = 2208988800

def sntp_client():
    client = socket.socket( socket.AF_INET,socket.SOCK_DGRAM )
    data = '\x1b' + 47 * '\0'
    client.sendto( data.encode('utf-8'),( NTP_SERVER, 123 ))
    data, address = client.recvfrom( 1024 )

    if data:
        print ('Response receivedfrom:', address)
    t = struct.unpack( '!12I', data )[10]
    t -= TIME1970
    print ('\tTime=%s' % time.ctime(t))
    
if __name__ == '__main__':
    sntp_client()