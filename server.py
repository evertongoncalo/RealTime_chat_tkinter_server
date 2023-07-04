import socket
import threading

HOST = 'localhost'  # Endereço do servidor (pode ser o IP ou 'localhost' para o próprio computador)
PORT = 8000  # Número da porta que deseja conectar

# Cria um objeto de socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()


salas = {}

def broadcast(sala, mensagem):
    for i in salas[sala]:
        if isinstance(mensagem,str):
            mensagem = mensagem.encode()
        i.send(mensagem)
        
def send_message(nome, sala, client):
    while True:
        mensagem = client.recv(1024)
        mensagem = f"{nome} :  {mensagem.decode()}\n"
        broadcast(sala, mensagem)
    


while True:

    # Conecta ao servidor
    
    client, addr = s.accept()
    client.send(b'SALA')
    
    sala = client.recv(1024).decode()
    nome = client.recv(1024).decode()
    
    if sala not in salas.keys():
        salas[sala] = []
    salas[sala].append(client)
    print(f"{nome} se conectou na sala: {sala}. INFO: {addr}")
    broadcast(sala, f"{nome} entrou na sala \n")
    
    thread = threading.Thread(target=send_message,args=(nome,sala,client))
    thread.start()

   



