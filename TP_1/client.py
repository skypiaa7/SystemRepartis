import socket

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 12345))
    while True:
        expression = input("Entrez une expression à calculer ou quit pour quitter: ")
        if expression.lower() == "quit":
            break
        client.sendall(expression.encode())
        if expression.lower() == 'quit_server':
            break
        result = client.recv(1024)
        print("Résultat: ", result.decode())
    client.close()

if __name__ == "__main__":
    start_client()
