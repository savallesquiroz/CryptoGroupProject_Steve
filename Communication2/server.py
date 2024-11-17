import socket
import threading
from crypto.crypto_utils import (
    generate_rsa_keys, decrypt_rsa, encrypt_aes, decrypt_aes
)

# Server Configuration
HOST = '127.0.0.1'
PORT = 65432

# RSA Key Pair (Server)
private_key, public_key = generate_rsa_keys()


# Function to handle each client
def handle_client(conn, addr):
    try:
        print(f"Connected by {addr}")

        # Step 1: Send the server's public key
        conn.sendall(public_key)

        # Step 2: Receive AES key encrypted with RSA
        encrypted_aes_key = conn.recv(256)
        aes_key = decrypt_rsa(private_key, encrypted_aes_key)
        print(f"Received AES key from {addr}")

        # Step 3: Handle encrypted communication
        while True:
            encrypted_message = conn.recv(1024)
            if not encrypted_message:
                break
            message = decrypt_aes(aes_key, encrypted_message)
            print(f"Message from {addr}: {message}")

            # Encrypt acknowledgment
            encrypted_response = encrypt_aes(aes_key, "Message received.")
            conn.sendall(encrypted_response)
    except Exception as e:
        print(f"Error with {addr}: {e}")
    finally:
        conn.close()
        print(f"Connection with {addr} closed.")


# Start the server
def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print(f"Server started. Listening on {HOST}:{PORT}...")

        while True:
            conn, addr = server_socket.accept()
            client_thread = threading.Thread(target=handle_client, args=(conn, addr))
            client_thread.start()


if __name__ == "__main__":
    start_server()
