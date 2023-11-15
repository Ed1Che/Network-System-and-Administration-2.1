import socket
import sys
import pickle

def start_server(host, port):
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to a specific address and port
    server_socket.bind((host, port))

    # Listen for incoming connections
    server_socket.listen(5)
    print(f"Server listening on {host}:{port}")

    while True:
        # Accept a connection from a client
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")

        # Receive and send back data
        data = client_socket.recv(4096)
        data = pickle.loads(data)
        print(f"Received data: {data}")

        exp=data
        a=exp[0]
        op=exp[1]
        b=exp[2]
        
        
        if (op != None):
            if  (op == 3):
                    data = a + b
                    data = [data]
            elif (op == 4):
                    data = a-b
                    data=[data]
            elif (op == 1):
                    data =  a*b
                    data = [data]
            elif (op == 2):
                data = a / b
                data = [data]
        else:
                    data = print ("Invalid operation...")
        
        # Echo the data back to the client
        
        data=pickle.dumps(data)
        client_socket.sendall(data)

        # Close the connection
        client_socket.close()

if __name__ == "__main__":
    # Set the host and port for the server
    host = "127.0.0.1"
    port = 37037

    # Start the server
    start_server(host, port)