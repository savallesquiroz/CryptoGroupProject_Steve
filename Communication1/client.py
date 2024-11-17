import socket
import rsa  # Lightweight built-in RSA module for Python

# Server Configuration
HOST = '127.0.0.1'
PORT = 65432

# Generate AES key
AES_KEY = b'supersecretkey!'  # Example: 16 bytes key


# Encrypt message using AES (simple XOR for demonstration)
def encrypt_message(message, aes_key):
    return bytes([b ^ aes_key[i % len(aes_key)] for i, b in enumerate(message.encode())])


# Decrypt message using AES (simple XOR for demonstration)
def decrypt_message(encrypted_message, aes_key):
    return ''.join(chr(b ^ aes_key[i % len(aes_key)]) for i, b in enumerate(encrypted_message))


def start_client():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((HOST, PORT))
            print("Connected to server.")

            # Step 1: Receive the server's public key
            server_public_key = rsa.PublicKey.load_pkcs1(client_socket.recv(450))

            # Step 2: Send AES key encrypted with RSA
            encrypted_aes_key = rsa.encrypt(AES_KEY, server_public_key)
            client_socket.sendall(encrypted_aes_key)
            print("Sent AES key to server.")

            # Step 3: Send encrypted messages
            while True:
                message = input("Enter your message (or 'quit' to exit): ")
                if message.lower() == 'quit':
                    break
                encrypted_message = encrypt_message(message, AES_KEY)
                client_socket.sendall(encrypted_message)

                # Receive and decrypt server response
                encrypted_response = client_socket.recv(1024)
                response = decrypt_message(encrypted_response, AES_KEY)
                print(f"Server replied: {response}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    start_client()
