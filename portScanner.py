import socket
import ipaddress

network_range = ""
# target_ip = ""
target_ports = [80, 443, 22, 24]

try:
    network = ipaddress.ip_network(network_range, strict=False)
    for ip in network.hosts():
        target_ip = str(ip)

        for target_port in target_ports:
            try:
                client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client_socket.settimeout(0.5)
                connection_response = client_socket.connect_ex((target_ip, target_port))

                if connection_response == 0:
                    print(f"{target_ip} open on port {target_port}")
                    client_socket.close()
                else:
                    print(f"{target_ip} closed on port {target_port}")

            except socket.error:
                print(f"Could not connect to {target_ip} on port {target_port}")

except ValueError:
    print(f"Error: '{network_range}' is not a valid network range.")
except KeyboardInterrupt:
    print("\nScan stopped by user.")

print("\n...Scan complete.")