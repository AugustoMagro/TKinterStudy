import tkinter as tk
import customtkinter as ck
from functionDB import *

class telaInclusao(ck.CTkFrame):
    def __init__(self, parent, salvarDados):
        super().__init__(master = parent)
        self.grid(column = 0, columnspan = 2, row = 0, sticky = 'nsew')
        self.salvarDados = salvarDados
        #caixa testo nome

        self.btLogin = ck.CTkButton(self, text="CLIKA", command= self.button_click).pack(expand=True)

    def button_click(self):
        nome = "nome"
        self.salvarDados(nome)
        dados = nome
        ConectarDB.__init__(self)
        ConectarDB.inserir_registro(self, dados)