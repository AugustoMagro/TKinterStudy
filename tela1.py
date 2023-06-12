import tkinter as tk
from tkinter import ttk
from tkinter import *
from typing import Callable, Optional, Tuple, Union
import customtkinter as ck
from functionDB import *

class Tela1(ck.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent, fg_color="transparent")
        self.grid(row=0, column=1, sticky="nsew")

        #Config frame principal
        self.rowconfigure(0, weight=2, uniform='a')
        self.rowconfigure(1, weight=1, uniform='a')
        self.grid_columnconfigure(0, weight=1, uniform='a')

        #Config frame Widgets
        self.frame1 = ck.CTkFrame(self, width=1)
        self.frame1.grid(row=0, column=0, sticky="nsew", pady=20, padx=20)
        self.frame1.grid_rowconfigure((0,1,2), weight=1, uniform='a')
        self.frame1.grid_columnconfigure((0, 1, 2), weight=1, uniform='a')
        self.frame1.grid_columnconfigure(3, weight=2, uniform='a')

        #Criando widgets
        self.titulo = ck.CTkLabel(self.frame1, text="INCLUSÃO DE ITEMS", font=("Arial Black", 25))
        self.entryNome = ck.CTkEntry(self.frame1, placeholder_text="Nome", border_width=0)
        self.entrySobrenome = ck.CTkEntry(self.frame1, placeholder_text="Sobrenome", border_width=0)
        self.entryCPF = ck.CTkEntry(self.frame1, placeholder_text="CPF", border_width=0)
        self.entryEmail = ck.CTkEntry(self.frame1, placeholder_text="Email", border_width=0)
        self.botaoInserir = ck.CTkButton(self.frame1, text="INSERIR", font=("Arial", 12),command=self.clikBotaoInserir)
        self.botaoProcurar = ck.CTkButton(self.frame1, text="PROCURAR", font=("Arial", 12),command=self.clikBotaoProcurar)
        self.listbox = tk.Listbox(self, font = "monospace")
        self.listbox.bind("<Double-Button-1>", self.duplo_clique)


        #Posicionado widgets
        self.titulo.grid(row=0, columnspan=4, pady=10, sticky="ew")
        self.entryNome.grid(row=1, column=0, padx=5, sticky="ew")
        self.entrySobrenome.grid(row=1, column=1, padx=5, sticky="ew")
        self.entryCPF.grid(row=1, column=2, padx=5, sticky="ew")
        self.entryEmail.grid(row=1, column=3, sticky="ew", padx=5)
        self.botaoInserir.grid(row=2, column=0, columnspan=2)
        self.botaoProcurar.grid(row=2, column=2,columnspan=2)
        self.listbox.grid(row=1, column=0, sticky="nsew", padx=20, pady=20)

    def clikBotaoInserir(self):
        Nome = self.entryNome.get()
        Sobrenome = self.entrySobrenome.get()
        CPF = self.entryCPF.get()
        Email = self.entryEmail.get()
        ConectarDB.__init__(self)
        ConectarDB.inserir_registro(self, Nome, Sobrenome, CPF, Email)
        self.entryNome.delete(0, 99)
        self.entrySobrenome.delete(0, 99)
        self.entryCPF.delete(0, 99)
        self.entryEmail.delete(0, 99)
    
    def clikBotaoProcurar(self):

        nome = self.entryNome.get()
        ConectarDB.__init__(self)
        self.lista = ConectarDB.consultar_registros(self, nome)

        self.longest_1 = max( len(x[1]) for x in self.lista )
        self.longest_2 = max( len(x[2]) for x in self.lista )
        self.longest_3 = max( len(x[3]) for x in self.lista )
        self.longest_4 = max( len(x[4]) for x in self.lista )

        i = 0
        for x in self.lista:
            line = '%s | %*s | %*s | %*s | %*s' % (x[0], -self.longest_1, x[1], -self.longest_2, x[2], -self.longest_3, x[3], -self.longest_4, x[4])
            self.listbox.insert(tk.END, line)
            i = i + 1
    
    def duplo_clique(self, *args):
        #Limpando entrys
        self.entryNome.delete(0, 99)
        self.entrySobrenome.delete(0, 99)
        self.entryCPF.delete(0, 99)
        self.entryEmail.delete(0, 99)

        #Selecionando item listbox
        i = self.listbox.index(ACTIVE)
        a = self.lista[i]
        self.entryCPF.insert(0,a[3])
        self.entryEmail.insert(0,a[4])
        self.entryNome.insert(0,a[1])
        self.entrySobrenome.insert(0,a[2])
