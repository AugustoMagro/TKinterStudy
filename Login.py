import tkinter as tk
import customtkinter as ck
from SETINGS import *
from typing import Callable, Optional, Tuple, Union
from tela1 import Tela1
from tkinter import *
from tkinter import messagebox
from random import choice
from functionDB import *


class Login(ck.CTkFrame):
    def __init__(self, parent, menu):
        super().__init__(master=parent, fg_color=FIRSTCOLOR)
        self.menu = menu

        #Config main frame
        self.grid(row=0, columnspan=2, sticky="nsew")
        self.rowconfigure(0, weight=1, uniform='a')
        self.rowconfigure(1, weight=1, uniform='a')
        self.grid_columnconfigure(0, weight=1, uniform='a')

        #Config second frame
        self.frame1 = ck.CTkFrame(self, width=1, fg_color=FIFTHCOLOR, corner_radius=CONERFRAME)
        self.frame1.grid(rowspan=2, column=0, sticky="nsew", padx=750, pady=230)
        self.frame1.grid_rowconfigure(0, weight=1, uniform='a')
        self.frame1.grid_rowconfigure(1, weight=1, uniform='a')
        self.frame1.grid_rowconfigure(2, weight=1, uniform='a')
        self.frame1.grid_rowconfigure(3, weight=1, uniform='a')
        self.frame1.grid_columnconfigure(0, weight=1, uniform='a')

        #Adding Widgets
        self.loginLabel = ck.CTkLabel(self.frame1,
                                      text="LOGIN",
                                      font=("Ebrima Bold", 35),
                                      text_color=FIRSTCOLOR)
        self.entryNomeLogin = ck.CTkEntry(self.frame1, 
                                          placeholder_text_color=FIRSTCOLOR,
                                          placeholder_text="Name",
                                          font=("Ebrima", 12),
                                          border_width=2, 
                                          border_color=FIRSTCOLOR, 
                                          fg_color="transparent",
                                          corner_radius=CORNERBUTTOM, 
                                          text_color=FIRSTCOLOR,
                                          width=189, height=32)
        self.entrySenhaLogin = ck.CTkEntry(self.frame1, 
                                          placeholder_text_color=FIRSTCOLOR,
                                          placeholder_text="Senha",
                                          font=("Ebrima", 12),
                                          border_width=2, 
                                          border_color=FIRSTCOLOR, 
                                          fg_color="transparent",
                                          corner_radius=CORNERBUTTOM, 
                                          text_color=FIRSTCOLOR,
                                          width=189, height=32,
                                          show='*')
        self.botaoLogin = ck.CTkButton(self.frame1, 
                                       text="Login", 
                                       font=("Ebrima", 12),
                                       border_width=2, 
                                       border_color=FIRSTCOLOR,
                                       fg_color=FIRSTCOLOR, 
                                       corner_radius=CORNERBUTTOM,
                                       hover_color=FIFTHCOLOR,
                                       command=self.button_login_click,
                                       anchor="center",
                                       width=150, height=47)
        
        #Placing widgets
        self.loginLabel.grid(row=0, column=0, sticky="s", pady=5)
        self.entryNomeLogin.grid(row=1, column=0, sticky="s", pady=5)
        self.entrySenhaLogin.grid(row=2, column=0, sticky="n", pady=5)
        self.botaoLogin.grid(row=3, column=0, sticky="n")
    
    def button_login_click(self):
        nome=self.entryNomeLogin.get()
        senha=self.entrySenhaLogin.get()
        banco="users_cadastro"
        ConectarDB.__init__(self)
        self.resultLogin = ConectarDB.consultar_registro_pela_id(self, nome, senha)

        if not self.resultLogin:
            messagebox.showerror("error", "SENHA INCORRETA")
        else:
            self.menu()