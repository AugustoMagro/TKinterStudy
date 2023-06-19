import tkinter as tk
import customtkinter as ck
from SETINGS import *
from typing import Callable, Optional, Tuple, Union
from tela1 import Tela1
from tkinter import *
from tkinter import messagebox


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
        self.frame1.grid_rowconfigure((0,1,2,3), weight=1, uniform='a')
        self.frame1.grid_columnconfigure(0, weight=1, uniform='a')

        #Adding Widgets
        self.entryNomeLogin = ck.CTkEntry(self.frame1, 
                                          placeholder_text_color=FIRSTCOLOR,
                                          placeholder_text="Name", 
                                          border_width=2, 
                                          border_color=FIRSTCOLOR, 
                                          fg_color="transparent",
                                          corner_radius=CORNERBUTTOM, 
                                          text_color=FIRSTCOLOR)
        self.botaoLogin = ck.CTkButton(self.frame1, 
                                       text="Login", 
                                       font=("Arial", 12),
                                       border_width=0, 
                                       fg_color=FIRSTCOLOR, 
                                       corner_radius=CORNERBUTTOM, 
                                       command=self.button_login_click)

        self.entryNomeLogin.grid(row=1, column=0, sticky="nsew", pady=50, padx=120)
        self.botaoLogin.grid(row=3, column=0, sticky="nsew", pady=50, padx=120)
    
    def button_login_click(self):
        if self.entryNomeLogin.get() == "":
            messagebox.showerror("error", "DIGITE SEU NOME")
        else:
            self.menu()