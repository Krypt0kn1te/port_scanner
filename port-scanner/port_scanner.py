import socket
def check_port(target, port, timeout=1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)

    result = sock.connect_ex((target, port))
    sock.close()

    if result == 0:
        return True
    else:
        return False

target = "scanme.nmap.org"
open_ports = []

for port in range (1, 1025):
    if check_port(target, port):
        print(f"Port {port} is OPEN")
        open_ports.append(port)


print(f"Scan complete. Open ports: {open_ports}")       




