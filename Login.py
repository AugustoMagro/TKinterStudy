import tkinter as tk
from typing import Callable, Optional, Tuple, Union
import customtkinter as ck
from tela1 import Tela1
from tkinter import *
from tkinter import messagebox


class Login(ck.CTkFrame):
    def __init__(self, parent, menu):
        super().__init__(master=parent)
        self.menu = menu

        self.grid(row=0, columnspan=2, sticky="nsew")
        self.rowconfigure(0, weight=1, uniform='a')
        self.rowconfigure(1, weight=1, uniform='a')
        self.grid_columnconfigure(0, weight=1, uniform='a')

        #Adding Widgets
        self.entryNomeLogin = ck.CTkEntry(self, placeholder_text="NOME", border_width=0)
        self.botaoLogin = ck.CTkButton(self, text="Login" , font=("Arial", 12),border_width=0 ,command=self.button_login_click)

        self.entryNomeLogin.grid(row=0, column=0, sticky="s", pady=10)
        self.botaoLogin.grid(row=1, column=0, sticky="n", pady=10)
    
    def button_login_click(self):
        if self.entryNomeLogin.get() == "":
            messagebox.showerror("error", "DIGITE SEU NOME")
        else:
            self.menu()