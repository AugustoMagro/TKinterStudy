import tkinter as tk
import customtkinter as ck
from PIL import Image, ImageTk
from menu import Menu
from Login import Login
from tela1 import Tela1
from tela2 import Tela2
from tela3 import Tela3
from tela4 import Tela4
from tela5 import Tela5

class App(ck.CTk):
    def __init__(self):

        #setup
        super().__init__()
        ck.set_appearance_mode("dark")
        self.geometry("1980x1080")
        self.minsize(600, 600)
        self.title("tela teste")
        self.iconbitmap(r"C:\Users\augus\OneDrive\Documentos\TelaPY\Images\4417105_cdn_connected_globe_dots_earth_icon.ico")


        #layout
        self.rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=2, uniform='a')
        self.grid_columnconfigure(1, weight=8, uniform='a')

        #Chamar tela login
        self.login = Login(self, self.menu)

        self.mainloop()

    # add methods to app
    def menu(self):
        self.login.grid_forget()
        self.menu = Menu(self, self.tela1, self.tela2, self.tela3, self.tela4, self.tela5)

    def salvarDados(self, nome):
        print(nome)
    
    def tela1(self):
        self.tela = Tela1(self)

    def tela2(self):
        self.tela2 = Tela2(self)

    def tela3(self):
        self.tela3 = Tela3(self)

    def tela4(self):
        self.tela4 = Tela4(self)

    def tela5(self):
        self.tela5 = Tela5(self)

App()

 