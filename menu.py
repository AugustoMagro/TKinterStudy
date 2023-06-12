import tkinter as tk
from typing import Callable, Optional, Tuple, Union
import customtkinter as ck
from tela1 import Tela1


class Menu(ck.CTkFrame):
    def __init__(self, parent, tela1, tela2, tela3, tela4, tela5):
        super().__init__(master=parent)
        self.grid(row=0, column=0, sticky="nsew")
        self.tela1 = tela1
        self.tela2 = tela2
        self.tela3 = tela3
        self.tela4 = tela4
        self.tela5 = tela5

        self.rowconfigure(0, weight=1, uniform='a')
        self.rowconfigure(1, weight=1, uniform='a')
        self.grid_columnconfigure(0, weight=1, uniform='a')

        self.buttonFrame = ck.CTkFrame(self, fg_color="transparent")
        self.buttonFrame.grid(row=0, column=0, sticky="nsew", pady=20)
        self.buttonFrame.grid_rowconfigure((1,2,3,4,5,6), weight=1, uniform='a')
        self.buttonFrame.grid_columnconfigure(0, weight=1, uniform='a')

        self.menuLabel = ck.CTkLabel(self.buttonFrame, text="MENU", font=("arial black", 22),)#.pack(expand=True)

        self.menuBotao1 = ck.CTkButton(self.buttonFrame, text="HOME" , font=("Arial", 12),command=self.button_home_event)#.pack(expand=True)
        self.menuBotao2 = ck.CTkButton(self.buttonFrame, text="INCLUSÃO" , font=("Arial", 12),command=self.button_home_event2)#.pack(expand=True)
        self.menuBotao3 = ck.CTkButton(self.buttonFrame, text="ATUALIZAÇÃO 1" , font=("Arial", 12),command=self.button_home_event3)#.pack(expand=True)
        self.menuBotao4 = ck.CTkButton(self.buttonFrame, text="ATUALIZAÇÃO 2" , font=("Arial", 12),command=self.button_home_event4)#.pack(expand=True)
        self.menuBotao5 = ck.CTkButton(self.buttonFrame, text="CONCLUSÃO" , font=("Arial", 12),command=self.button_home_event5)#.pack(expand=True)

        self.menuLabel.grid(row=1, column=0)
        self.menuBotao1.grid(row=2, column=0)
        self.menuBotao2.grid(row=3, column=0)
        self.menuBotao3.grid( row=4, column=0)
        self.menuBotao4.grid( row=5, column=0)
        self.menuBotao5.grid( row=6, column=0)


    def button_home_event(self):
        self.tela1()
    
    def button_home_event2(self):
        self.tela2()

    def button_home_event3(self):
        self.tela3()

    def button_home_event4(self):
        self.tela4()

    def button_home_event5(self):
        self.tela5()

        
