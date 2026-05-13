import socket

target = input("Enter IP address: ")

open_ports = []


for port in range(1, 1025):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)

    result = s.connect_ex((target, port))

    if result == 0:
        print(f"Port {port} is OPEN")
        open_ports.append(port)

    s.close()

print("\nTotal Open Ports:", len(open_ports))
print("Open Ports List:", open_ports)