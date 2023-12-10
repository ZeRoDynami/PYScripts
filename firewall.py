import socket
import threading

class SimpleFirewall:
    def __init__(self):
        self.allowed_ports = {80, 443}  # Specify the ports you want to allow

    def start_firewall(self, port):
        firewall_thread = threading.Thread(target=self._firewall, args=(port,))
        firewall_thread.start()

    def _firewall(self, port):
        firewall_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        firewall_socket.bind(("0.0.0.0", port))
        firewall_socket.listen(5)

        print(f"Firewall started on port {port}")

        while True:
            client_socket, addr = firewall_socket.accept()
            client_ip, client_port = addr

            if client_port not in self.allowed_ports:
                print(f"Blocked connection from {client_ip}:{client_port}")
                client_socket.close()
            else:
                print(f"Allowed connection from {client_ip}:{client_port}")
                client_socket.send(b"Connection allowed.")
                client_socket.close()

if __name__ == "__main__":
    firewall = SimpleFirewall()
    firewall_port = 8888  # Choose a port for the firewall

    firewall.start_firewall(firewall_port)
