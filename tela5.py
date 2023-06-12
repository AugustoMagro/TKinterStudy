import tkinter as tk
from typing import Callable, Optional, Tuple, Union
import customtkinter as ck

class Tela5(ck.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent, fg_color="pink")
        self.grid(row=0, column=1, sticky="nsew")
