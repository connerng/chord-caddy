from transposer import *
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from chordprog import *

chords = ['.','Ab', 'Abm', 'A', 'Am', 'A#', 'A#m', 'Bb', 'Bbm', 'B', 'Bm', 'C', 'Cm', 'C#', 'C#m', 'Db', 'Dbm', 
          'D', 'Dm', 'D#', 'D#m', 'Eb', 'Ebm', 'E', 'Em', 'F', 'Fm', 'F#', 'F#m', 'Gb', 'Gbm', 'G', 'Gm', 
          'G#', 'G#m']

keys = ['Ab', 'A', 'A#', 'Bb', 'B', 'C', 'C#', 'Db', 'D', 'D#', 'Eb', 'E', 'F', 'F#', 'Gb', 'G', 'G#']

def save_clicked():
    cpStr = "|"
    for i in range(0, len(chordProgCB)):
        cpStr += chordProgCB[i].get()
        if (i+1)%4 == 0:
            cpStr += "|"
    cp = ChordProgression(cpStr, time_signature, key.get())
    chordsDisplay['text'] = cp.ToString()
    keyDisplay['text'] = "Key: " + cp.key

def transpose_clicked():
    cpStr = "|"
    for i in range(0, len(chordProgCB)):
        cpStr += chordProgCB[i].get()
        if (i+1)%4 == 0:
            cpStr += "|"
    cp = ChordProgression(cpStr, time_signature, key.get())
    cp = TransposeCP(cp, semitoneScale.get())
    cp_new = cp.ToString()
    print(cp_new)
    chordsDisplay['text'] = cp.ToString()
    keyDisplay['text'] = "Key: " + cp.key

def create_new_clicked():
    print("Create New Progression")

def play_clicked():
    print("Play")

def lib_clicked():
    print("Library")

root = tk.Tk()
root.title("Chord Transposer")
root.geometry('750x450')

style = ttk.Style()
style.theme_use('vista')

mainmenu = tk.Menu(root)
mainmenu.add_command(label = "Create New", command = create_new_clicked)
mainmenu.add_command(label = "Play", command=play_clicked)
mainmenu.add_command(label = "Library", command=lib_clicked)
root.config(menu = mainmenu)



new_cp_title = ttk.Label(root, text="Create New Chord Progression", font=('Helvetica', 14))
new_cp_title.place(x = 10, y = 0)

lbl_timeSig = ttk.Label(root, text="Time Signature: 4/4")
lbl_timeSig.place(x=10, y=30)

lbl_key = ttk.Label(root, text="Key")
lbl_key.place(x=10, y=55)

lbl_measure1 = ttk.Label(root, text="Measure 1")
lbl_measure1.place(x=10, y=80)
lbl_measure2 = ttk.Label(root, text="Measure 2")
lbl_measure2.place(x=10, y=105)
lbl_measure3 = ttk.Label(root, text="Measure 3")
lbl_measure3.place(x=10, y=130)
lbl_measure4 = ttk.Label(root, text="Measure 4")
lbl_measure4.place(x=10, y=155)

time_signature = "4/4"
chordProgCB = []
for r in range(0, 4):
    for col in range(1, 5):
        cur = ttk.Combobox(root, values=chords, state='readonly', width=5)
        cur.current(0)
        cur.place(x = (col * 50) + 25, y = (r * 25) + 80)
        chordProgCB.append(cur)

key = tk.StringVar()
keys = ttk.Combobox(root, values=keys, state='readonly', width=5, textvariable=key)
keys.place(x=75, y=55)

chordsDisplay = ttk.Label(root, text="| . . . . | . . . . | . . . . | . . . . |", font=('Helvetica', 16), background="light yellow")
chordsDisplay.place(x=290, y=100)

keyDisplay = ttk.Label(root, text="Key: ", font=('Helvetica', 16), background="light yellow")
keyDisplay.place(x=290, y=70)

saveButton = ttk.Button(root, text="Save", width=25, command=save_clicked)
saveButton.place(x=10, y=185)

transposeButton = ttk.Button(root, text = "Transpose", width=25, command=transpose_clicked)
transposeButton.place(x=10, y=300)

semitoneScale = tk.Scale(root, from_=-6, to=6, orient='horizontal', length=150)
semitoneScale.place(x=10, y=250)

root.mainloop()