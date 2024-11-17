### CSCI663 - Introduction to Cryptography
### Steve Valles
### Final Project


# Secure Client-Server Communication 



## Description
This project implements a secure communication system between a client and server using Python. It incorporates RSA for secure key exchange and basic XOR-based encryption for symmetric communication. The server is capable of handling multiple clients simultaneously through multithreading.  

## Getting Started
I have created two options for the group, one that uses the `pycryptodome` library, allowing for stronger AES encryption and another that does not use said library. For Communication2(the one that makes use of `pycryptodome` library), the file crypto_utils.py located on Crypto directory is needed. For Communication1, this file has to be ignored. For the rest of the README file there will be instructions for both, once decided which one to keep, delete the other one.
### Dependencies
COMMUNICATION1
- Python 3.x  
- rsa library for key generation and encryption:  
  pip install rsa  
- 
COMMUNICATION2
Ensure the following are installed on your system:  
- Python 3.8+  
- `pycryptodome` library for cryptographic operations. 

### Installing

```
pip install -r requirements. txt
```

### Executing program

* Start the server:  
  python server.py (This will launch the server to listen for client connections.)  

* Start the client:  
  python client.py (This will launch the client to connect to the server.)  

* Enter a message in the client terminal to send it to the server. The server will respond with an acknowledgment.  

* To exit the client, type quit.



## License

This project is licensed under the MIT License - see the `LICENSE` file for details.

## Acknowledgments
COMMUNICATION 1
* [rsa library documentation](https://stuvel.eu/rsa)
* 
COMMUNICATION 2
Inspiration, code snippets, etc.
* [pycryptodome documentation](https://www.pycryptodome.org/)
* [Python socket programming tutorial](https://realpython.com/python-sockets/)
* [Multithreading in Python](https://docs.python.org/3/library/threading.html)

