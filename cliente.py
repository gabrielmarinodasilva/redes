import socket
import threading

HOST = '127.0.0.1'  # IP do servidor
PORT = 12345

def receber(sock):
    while True:
        try:
            msg = sock.recv(1024)
            if not msg:
                break
            print(f"\nMensagem recebida: {msg.decode().strip()}")
        except:
            break

# Conecta ao servidor
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

print("Conectado. Digite mensagens para enviar ao outro cliente.")
print("Use Ctrl+C ou 'q' para sair.\n")

# Thread para receber mensagens
thread = threading.Thread(target=receber, args=(sock,), daemon=True)
thread.start()

try:
    while True:
        msg = input("Você: ")
        if msg.strip().lower() == 'q':
            break
        sock.sendall(msg.encode())
except KeyboardInterrupt:
    pass

print("Encerrando cliente...")
sock.close()
