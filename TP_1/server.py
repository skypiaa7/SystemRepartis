import socket

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 12345))
    server.listen()
    conn, addr = server.accept()
    while True:
        conn, addr = server.accept()
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

if __name__ == "__main__":
    start_server()
