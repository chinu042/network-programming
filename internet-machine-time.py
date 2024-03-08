# Printing the current time from the internet time server

'''In order to synchronize your machine time with one of the internet time servers, you can
write a Python client for that. For this, ntplib will be used. Here, the client/server
conversation will be done using Network Time Protocol (NTP).'''

'''Here, an NTP client has been created and an NTP request has been sent to one of the
internet NTP servers, pool.ntp.org. The ctime() function is used for printing the
response.'''

import ntplib
from time import ctime

def print_time():
    ntp_client = ntplib.NTPClient()
    response = ntp_client.request('pool.ntp.org')
    print(ctime(response.tx_time))

if __name__ == "__main__":
    print_time()