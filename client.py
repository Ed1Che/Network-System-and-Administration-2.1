import socket
import sys 
import pickle

try: 
    client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error as err:
    print("Failed to create socket")
    SystemExit
print("socket created")

shost = "127.0.0.1"
sport = 37037

try:
    client_socket.connect((shost,sport))
    print("Connected to server")
    a = None
    b = None
    op = None

    a = int(input("Enter the first argument: "))
    op = int (input("Enter the operation(1(*),2(/),3(+),4(-): "))
    b = int(input("Enter the second argument: "))

    exp= [a,op,b]
    dat=pickle.dumps(exp)

    # Send a message to the server
    client_socket.sendall(dat)
    

    # Receive the echoed message from the server
    data = client_socket.recv(4096)
    data = pickle.loads(data)

    if (op != None):
            if  (op == 3):
                    print(f" Sum received from server: {data}")
            elif (op == 4):
                     print(f" Difference received from server: {data}")
            elif (op == 1):
                     print(f" Product received from server: {data}")
            elif (op == 2):
                 print(f" Quotient received from server: {data}")
    else:
                 print ("Invalid operation...")
    
except socket.error as err:
    print("Error in connection")
    SystemExit