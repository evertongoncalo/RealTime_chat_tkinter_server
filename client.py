import socket
import threading
from tkinter import *
import tkinter
from tkinter import simpledialog
import customtkinter

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
        self.root = customtkinter.CTk()
        self.root.geometry('800x800')
        self.root.title('Chat Group')
        self.root._set_appearance_mode('dark')
    
        
        self.text_box = customtkinter.CTkTextbox(self.root, width=700,height=600,corner_radius=10,border_color='blue') #onde se localiza:
        self.text_box.place(relx=0.05, rely=0.05, )
        
        self.send_message = Entry(self.root) #onde se localiza o botao
        self.send_message.place(relx=0.05, rely=0.85, width=500,height=30)
        
        self.btn_send = customtkinter.CTkButton(self.root, text="Enviar",command=self.enviar_mensagem, width=50,height=30, hover_color=('green'), font=('', 20),corner_radius=2)
        self.btn_send.place(relx=0.70, rely=0.85)
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        
        self.root.mainloop()#faz a janela ficar aberta
        
    def close(self):  #fechar quando clicar
        self.root.destroy()
        self.root.quit
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
