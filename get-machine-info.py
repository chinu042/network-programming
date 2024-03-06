import socket

def print_machine_info():
    host_name=socket.gethostname()
    ip_address=socket.gethostbyname(host_name)
    print("Host name: %s" %host_name)
    print("IP address: %s" %ip_address)

def get_remote_machine_info():
    remote_host =  'www.google.com'
    try:
        print("IP address of remote %s: %s" %(remote_host,socket.gethostbyname(remote_host)))
    except socket.error as err_msg:
        print("%s, %s" %(remote_host,err_msg))


if __name__ == "__main__":
    print_machine_info()
    get_remote_machine_info()