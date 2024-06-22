import tkinter as tk
from tkinter import ttk

def ShowNewProgression(window, cp_str):
    cp = ttk.Label(window, text=cp_str, font=('Helvetica', 18), justify="center", anchor="center", background="light yellow")
    cp.place(x = 290, y = 100)

    