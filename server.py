import socket
import threading

SERVER = "127.0.0.1"
PORT = 5555
IP_ADDRESS = (SERVER, PORT)
CLIENTS = {}


def setup():
    global SERVER, PORT, IP_ADDRESS
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(IP_ADDRESS)
        server.listen(100)
        print("Server is listening...")

        acceptConnections(server)
    except socket.error as e:
        print(f"Socket error: {e}")


def acceptConnections(server):
    try:
        while True:
            client_socket, client_address = server.accept()
            print(f"Connection established with {client_address}")
            thread = threading.Thread(
                target=handleClient, args=(client_socket,))
            thread.start()
    except socket.error as e:
        print(f"Error accepting connections: {e}")


def handleClient(client_socket):
    try:
        # Handle client logic here
        pass
    except socket.error as e:
        print(f"Error handling client: {e}")
    finally:
        client_socket.close()


if __name__ == "__main__":
    setup()
