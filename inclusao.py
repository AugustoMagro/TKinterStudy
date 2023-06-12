import tkinter as tk
import customtkinter as ck
from functionDB import *

#ck.set_appearance_mode("system")  # default
#ck.set_appearance_mode("dark")
ck.set_appearance_mode("light")

class telaInclusao(ck.CTkFrame):
    def __init__(self, parent, salvarDados):
        super().__init__(master = parent)
        self.salvarDados = salvarDados

        self.home_frame = ck.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)

        self.home_frame_large_image_label = ck.CTkLabel(self, text="")
        self.home_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)

        self.home_frame_button_1 = ck.CTkButton(self, text="")
        self.home_frame_button_1.grid(row=1, column=0, padx=20, pady=10)

        self.home_frame_button_2 = ck.CTkButton(self, text="CTkButton", compound="right")
        self.home_frame_button_2.grid(row=2, column=0, padx=20, pady=10)

        self.home_frame_button_3 = ck.CTkButton(self, text="CTkButton", compound="top")
        self.home_frame_button_3.grid(row=3, column=0, padx=20, pady=10)

        self.home_frame_button_4 = ck.CTkButton(self, text="CTkButton", compound="bottom", anchor="w")
        self.home_frame_button_4.grid(row=4, column=0, padx=20, pady=10)

    def button_click(self):
        nome = "nome"
        self.salvarDados(nome)
        dados = nome
        ConectarDB.__init__(self)
        ConectarDB.inserir_registro(self, dados)