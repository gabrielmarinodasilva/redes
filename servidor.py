import socket
import threading

HOST = '0.0.0.0'
PORT = 12345

clients = []

def handle_client(conn, addr):
    print(f"Cliente conectado: {addr}")
    while True:
        try:
            msg = conn.recv(1024)
            if not msg:
                break
            print(f"[{addr}] {msg.decode().strip()}")

            # Repassa mensagem 
            for client in clients:
                if client != conn:
                    client.sendall(msg)
        except:
            break

    print(f"Cliente desconectado: {addr}")
    clients.remove(conn)
    conn.close()

# Inicia o servidor
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print(f"Servidor ouvindo em {HOST}:{PORT}...")

while True:
    conn, addr = server.accept()
    clients.append(conn)
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()
