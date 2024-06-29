from transposer import *
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from chordprog import *
from view import *

chords = ['.','Ab', 'Abm', 'A', 'Am', 'A#', 'A#m', 'Bb', 'Bbm', 'B', 'Bm', 'C', 'Cm', 'C#', 'C#m', 'Db', 'Dbm', 
          'D', 'Dm', 'D#', 'D#m', 'Eb', 'Ebm', 'E', 'Em', 'F', 'Fm', 'F#', 'F#m', 'Gb', 'Gbm', 'G', 'Gm', 
          'G#', 'G#m']

keys = ['.', 'Ab', 'A', 'A#', 'Bb', 'B', 'C', 'C#', 'Db', 'D', 'D#', 'Eb', 'E', 'F', 'F#', 'Gb', 'G', 'G#']

global time_signature

def show(widget):
    widget.pack()

def hide(widget):
    widget.pack_forget()

def save_clicked():
    cpStr = "|"
    for i in range(0, len(chordProgCB)):
        cpStr += chordProgCB[i].get()
        if (i+1)%4 == 0:
            cpStr += "|"
    cp = ChordProgression(cpStr, time_signature, keysCB.get())
    chordsDisplay['text'] = cp.ToString()
    keyDisplay['text'] = "Key: " + cp.key

def transpose_clicked():
    cpStr = "|"
    for i in range(0, len(chordProgCB)):
        cpStr += chordProgCB[i].get()
        if (i+1)%4 == 0:
            cpStr += "|"
    cp = ChordProgression(cpStr, time_signature, keysCB.get())
    cp = TransposeCP(cp, semitoneScale.get())
    cp_new = cp.ToString()
    print(cp_new)
    chordsDisplay['text'] = cp.ToString()
    keyDisplay['text'] = "Key: " + cp.key

def ts_44_clicked():
    create_new_clicked()
    global chordProgCB
    chordProgCB = []
    for r in range(1, 5):
        for col in range(1, 5):
            cur = ttk.Combobox(root, values=chords, state='readonly', width=5)
            cur.current(0)
            cur.place(x = (col * 50) + 100, y = (r * 25) + 60)
            chordProgCB.append(cur)
    

def ts_68_clicked():
    create_new_clicked()
    global chordProgCB
    chordProgCB = []
    for r in range(1, 5):
        for col in range(1, 7):
            cur = ttk.Combobox(root, values=chords, state='readonly', width=5)
            cur.current(0)
            cur.place(x = (col * 50) + 50, y = (r * 25) + 60)
            chordProgCB.append(cur)

def create_new_clicked():
    clearWindow()
    keysList = keys
    root['bg'] = 'light yellow'
    new_cp_title = ttk.Label(root, text="Create New Chord Progression", font=('Helvetica', 14), background='light yellow')
    new_cp_title.pack()

    lbl_timeSig = ttk.Label(root, text="Time Signature:", font=('Helvetica', 10), background='light yellow')
    lbl_timeSig.pack()

    ts_44_button = ttk.Button(root, text="4/4", width=10, command=ts_44_clicked)
    ts_44_button.place(x=180, y=50)

    ts_68_button = ttk.Button(root, text="6/8", width=10, command=ts_68_clicked)
    ts_68_button.place(x=250, y=50)

    lbl_key = ttk.Label(root, text="Key: ", font=('Helvetica', 10), background='light yellow')
    lbl_key.place(x=150, y=190)

    keysCB = ttk.Combobox(root, values=keysList, state='readonly', width=5)
    keysCB.current(0)
    keysCB.place(x=200, y=190)

    lbl_cpname = ttk.Label(root, text="Name: ", font=('Helvetica', 10), background='light yellow')
    lbl_cpname.place(x=150, y=215)

    cp_name_entry = ttk.Entry(root)
    cp_name_entry.place(x=200, y=215)

    saveButton = ttk.Button(root, text="Save", width=10, command=save_clicked)
    saveButton.place(x=215, y=245)


def play_clicked():
    print("Play")

def lib_clicked():
    print("Library")

root = tk.Tk()
root.title("Chord Caddy")
root.geometry('500x300')

style = ttk.Style()
style.theme_use('vista')

mainmenu = tk.Menu(root)
mainmenu.add_command(label = "Create New", command = create_new_clicked)
mainmenu.add_command(label = "Play", command=play_clicked)
mainmenu.add_command(label = "Library", command=lib_clicked)
root.config(menu = mainmenu)

def clearWindow():
    for widget in root.winfo_children():
        widget.destroy()
    mainmenu = tk.Menu(root)
    mainmenu.add_command(label = "Create New", command = create_new_clicked)
    mainmenu.add_command(label = "Play", command=play_clicked)
    mainmenu.add_command(label = "Library", command=lib_clicked)
    root.config(menu = mainmenu)

root.mainloop()