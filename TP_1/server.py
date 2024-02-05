import socket
import threading

def handle_client(conn):
    while True:
        data = conn.recv(1024)
        if not data:
            break
        expression = data.decode()
        if expression.lower() == 'quit_server':
            conn.close()
            return
        try:
            result = eval(expression)
            conn.sendall(str(result).encode())
        except Exception as e:
            conn.sendall(str(e).encode())
    conn.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 12345))
    server.listen()
    while True:
        conn, addr = server.accept()
        client_thread = threading.Thread(target=handle_client, args=(conn,))
        client_thread.start()

if __name__ == "__main__":
    start_server()