import socket
import threading

class DDoSDetector:
    def __init__(self, listen_port=8888, threshold=5):
        # Initialize the DDoSDetector with default values
        self.listen_port = listen_port  # Listening port for the server
        self.threshold = threshold  # Connection count threshold for potential DDoS
        self.connection_count = 0  # Counter for incoming connections

    def start_server(self):
        # Create a server socket, bind it to the specified port, and start listening
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(("0.0.0.0", self.listen_port))
        server_socket.listen(5)

        print(f"DDoS Detector started on port {self.listen_port}")

        while True:
            # Accept incoming connections and handle each one in a separate thread
            client_socket, addr = server_socket.accept()
            threading.Thread(target=self.handle_client, args=(client_socket, addr)).start()

    def handle_client(self, client_socket, addr):
        # Process each incoming connection
        self.connection_count += 1  # Increment connection count
        print(f"Connection from {addr}. Total connections: {self.connection_count}")

        # Check if the connection count exceeds the threshold
        if self.connection_count > self.threshold:
            print(f"Potential DDoS attack detected! Connection count: {self.connection_count}")
            # Add your DDoS mitigation logic here (e.g., logging, blocking, etc.)

        # Send a simple acknowledgment message to the client
        client_socket.send(b"Connection accepted.")
        client_socket.close()

    def run_detector(self):
        # Start the DDoS detector in a separate thread
        server_thread = threading.Thread(target=self.start_server)
        server_thread.start()

if __name__ == "__main__":
    # Create an instance of DDoSDetector with custom settings
    ddos_detector = DDoSDetector(listen_port=8888, threshold=5)
    
    # Run the DDoS detector
    ddos_detector.run_detector()
