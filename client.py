import socket
import threading
from tkinter import *
import tkinter
from tkinter import simpledialog

class Chat:
    def __init__(self):
        HOST = 'localhost'
        PORT = 8000 
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((HOST,PORT))
        login = Tk()
        login.withdraw()
        
        self.window_loaded = False
        self.active = True 
        
        self.nome = simpledialog.askstring('Nome','Digite seu nome: ', parent=login)
        self.sala = simpledialog.askstring('Sala','Digite a sala: ', parent=login)
        
        thread = threading.Thread(target=self.conn)
        thread.start()
        
              
        self.window()
        
    def window(self):
        self.root = Tk()
        self.root.geometry('800x800')
        self.root.title('Chat Group')
        
        self.text_box = Text(self.root) #onde se localiza:
        self.text_box.place(relx=0.05, rely=0.05, width=700,height=600)
        
        self.send_message = Entry(self.root) #onde se localiza o botao
        self.send_message.place(relx=0.05, rely=0.85, width=500,height=30)
        
        self.btn_send = Button(self.root, text="Enviar", command=self.enviar_mensagem)
        self.btn_send.place(relx=0.70, rely=0.85, width=50,height=30)
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        
        self.root.mainloop()#faz a janela ficar aberta
        
    def close(self):  #fechar quando clicar
        self.root.destroy()
        self.client.close()
        
        
        
    def conn(self):
        while True:
            received = self.client.recv(1024)
            if received == b'SALA':
                self.client.send(self.sala.encode())
                self.client.send(self.nome.encode())
            else:
                try:
                    self.text_box.insert('end', received.decode())
                except:
                    pass
                
            
        
    def enviar_mensagem(self):
        mensagem = self.send_message.get()
        self.client.send(mensagem.encode())
        
        
        
        
        
        
chat = Chat()
