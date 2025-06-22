from datetime import datetime
import socket 
import threading 

HOST = '0.0.0.0' 
PORT = 12345 

clients = []

from datetime import datetime

def handle_client(conn, addr):
    print(f"Cliente conectado: {addr}")
    while True:
        try:
            msg = conn.recv(1024)
            if not msg:
                break

            decoded_msg = msg.decode().strip()
            print(f"[{addr}] {decoded_msg}")

            if decoded_msg.lower() == 'd':
                # Responde apenas ao cliente solicitante com data/hora atual
                now = datetime.now().strftime( ' %d/%m/%Y %H:%M:%S ')
                conn.sendall(f"Data e hora do servidor: {now}\n".encode())
            else:
                # Repassa a mensagem aos outros clientes
                for client in clients:
                    if client != conn:
                        client.sendall(f"[{addr}] {decoded_msg}".encode())
        except:
            break

    print(f"Cliente desconectado: {addr}")
    clients.remove(conn)
    conn.close()



server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.bind((HOST, PORT))
server.listen()

print(f"Servidor ouvindo em {HOST}:{PORT}...") 

while True:
    conn, addr = server.accept()
    clients.append(conn)
    thread = threading.Thread(target=handle_client, args=(conn, addr)) 
    thread.start()

