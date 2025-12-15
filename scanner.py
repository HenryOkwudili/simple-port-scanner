import socket # Socket module handles network connections

target_ip = "127.0.0.1"
target_port = 80

# 1. Create a socket object
# AF_INET specifies we are using IPv4
# SOCK_STREAM specifies this is a TCP connection

try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #2. Try to connect to the target IP and port
    # The connect_ex() method returns 0 if the connection is successful
    connection_result = client_socket.connect_ex((target_ip, target_port))

    #3. Check the result and print the message
    if connection_result == 0:
        print(f"Port {target_port} is open on {target_ip}")
    else:
        print(f"Port {target_port} is closed on {target_ip}")

    #4.  Close the socket connection
    client_socket.close()

except socket.error:
    print("Error: could not connect to the server.")