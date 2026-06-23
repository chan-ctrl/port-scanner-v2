import socket

target = input("Enter IP Address:")

start_port = int(input("Enter Starting Port:"))
end_port = int(input("Enter Ending Port:"))

print("\nScanning...\n")

for port in range(start_port, end_port + 1):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)

    result = sock.connect_ex((target, port))

    if result == 0:
        print(f"Port {port}: Open")
else:
    print(f"Port {port}: Closed")