import socket

HOST = "192.168.29.1"  # Replace with your laptop's IP
PORT = 12345           # Must match the client

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print(f"[LISTENING] Waiting for connection on {HOST}:{PORT}...")
conn, addr = server.accept()
print(f"[CONNECTED] Device connected from {addr}")

while True:
    command = input("Enter command (or 'exit' to quit): ").strip()

    if not command:
        continue  # Ignore empty input
    
    conn.send(command.encode())

    if command.lower() == "exit":
        break

    output = conn.recv(4096).decode()
    print(output)

conn.close()
server.close()
print("[DISCONNECTED] Connection closed.")
