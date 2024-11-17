import socket
import threading
import rsa  # Lightweight built-in RSA module for Python

# Server Configuration
HOST = '127.0.0.1'
PORT = 65432

# Generate RSA Key Pair
(public_key, private_key) = rsa.newkeys(2048)


# Function to handle each client
def handle_client(conn, addr):
    try:
        print(f"Connected by {addr}")

        # Step 1: Send the server's public key
        conn.send(public_key.save_pkcs1())

        # Step 2: Receive AES key encrypted with RSA
        encrypted_aes_key = conn.recv(256)
        aes_key = rsa.decrypt(encrypted_aes_key, private_key)
        print(f"Received AES key from {addr}")

        # Step 3: Handle encrypted communication
        while True:
            encrypted_message = conn.recv(1024)
            if not encrypted_message:
                break
            # Decrypt message
            message = decrypt_message(encrypted_message, aes_key)
            print(f"Message from {addr}: {message}")

            # Encrypt acknowledgment
            encrypted_response = encrypt_message("Message received.", aes_key)
            conn.sendall(encrypted_response)
    except Exception as e:
        print(f"Error with {addr}: {e}")
    finally:
        conn.close()
        print(f"Connection with {addr} closed.")


# Encrypt message using AES (simple XOR for demonstration)
def encrypt_message(message, aes_key):
    return bytes([b ^ aes_key[i % len(aes_key)] for i, b in enumerate(message.encode())])


# Decrypt message using AES (simple XOR for demonstration)
def decrypt_message(encrypted_message, aes_key):
    return ''.join(chr(b ^ aes_key[i % len(aes_key)]) for i, b in enumerate(encrypted_message))


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
