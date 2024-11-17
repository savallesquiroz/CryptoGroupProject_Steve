import socket
from crypto.crypto_utils import (
    generate_aes_key, encrypt_rsa, encrypt_aes, decrypt_aes
)

# Server Configuration
HOST = '127.0.0.1'
PORT = 65432


def start_client():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((HOST, PORT))
            print("Connected to server.")

            # Step 1: Receive the server's public key
            server_public_key = client_socket.recv(450)

            # Step 2: Generate AES key and send it encrypted with RSA
            aes_key = generate_aes_key()
            encrypted_aes_key = encrypt_rsa(server_public_key, aes_key)
            client_socket.sendall(encrypted_aes_key)
            print("Sent AES key to server.")

            # Step 3: Send encrypted messages
            while True:
                message = input("Enter your message (or 'quit' to exit): ")
                if message.lower() == 'quit':
                    break
                encrypted_message = encrypt_aes(aes_key, message)
                client_socket.sendall(encrypted_message)

                # Receive and decrypt server response
                encrypted_response = client_socket.recv(1024)
                response = decrypt_aes(aes_key, encrypted_response)
                print(f"Server replied: {response}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    start_client()
