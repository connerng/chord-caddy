from transposer import *
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from chordprog import *

chords = ['.','Ab', 'Abm', 'A', 'Am', 'A#', 'A#m', 'Bb', 'Bbm', 'B', 'Bm', 'C', 'Cm', 'C#', 'C#m', 'Db', 'Dbm', 
          'D', 'Dm', 'D#', 'D#m', 'Eb', 'Ebm', 'E', 'Em', 'F', 'Fm', 'F#', 'F#m', 'Gb', 'Gbm', 'G', 'Gm', 
          'G#', 'G#m']

keys = ['Ab', 'A', 'A#', 'Bb', 'B', 'C', 'C#', 'Db', 'D', 'D#', 'Eb', 'E', 'F', 'F#', 'Gb', 'G', 'G#']

root = tk.Tk()
root.title("Chord Transposer")
root.geometry('1000x600')

lbl_timeSig = ttk.Label(root, text="Time Signature")
lbl_timeSig.grid(column=0, row=0)

lbl_key = ttk.Label(root, text="Key")
lbl_key.grid(column=0, row=1)

lbl_measure1 = ttk.Label(root, text="Measure 1")
lbl_measure1.grid(column=0, row=2)
lbl_measure2 = ttk.Label(root, text="Measure 2")
lbl_measure2.grid(column=0, row=3)
lbl_measure3 = ttk.Label(root, text="Measure 3")
lbl_measure3.grid(column=0, row=4)
lbl_measure4 = ttk.Label(root, text="Measure 4")
lbl_measure4.grid(column=0, row=5)

time_signature = "4/4"
chordProgCB = []
for r in range(2, 6):
    for col in range(1, 5):
        cur = ttk.Combobox(root, values=chords, state='readonly', width=5)
        cur.current(0)
        cur.grid(column=col, row=r)
        chordProgCB.append(cur)


def ts_44_clicked():
    for cb in chordProgCB:
        cb.destroy()
    chordProgCB = []
    for r in range(2, 6):
        for col in range(1, 5):
            cur = ttk.Combobox(root, values=chords, state='readonly', width=5)
            cur.current(0)
            cur.grid(column=col, row=r)
            chordProgCB.append(cur)

timeSig_44 = ttk.Button(root, text="4/4", width=5, command=ts_44_clicked)
timeSig_44.grid(column=1, row=0)

def ts_68_clicked():
    for cb in chordProgCB:
        cb.destroy()
    chordProgCB = []
    for r in range(2, 6):
        for col in range(1, 7):
            cur = ttk.Combobox(root, values=chords, state='readonly', width=5)
            cur.current(0)
            cur.grid(column=col, row=r)
            chordProgCB.append(cur)

timeSig_68 = ttk.Button(root, text="6/8", width=5, command=ts_68_clicked)
timeSig_68.grid(column=2, row=0)

key = tk.StringVar()
keys = ttk.Combobox(root, values=keys, state='readonly', width=5, textvariable=key)
keys.grid(column=1,row=1)




def clicked():
    if time_signature == "4/4":
        cpStr = "|"
        for i in range(0, len(chordProgCB)):
            cpStr += chordProgCB[i].get()
            if (i+1)%4 == 0:
                cpStr += "|"
    else:
        cpStr = "|"
        for i in range(0, len(chordProgCB)):
            cpStr += chordProgCB[i].get()
            if (i+1)%6 == 0:
                cpStr += "|"
    cp = ChordProgression(cpStr, time_signature, key.get())
    showinfo(title="New Chord Progression", message=cp.ToString())

saveButton = ttk.Button(root, text="Save", width=50, command=clicked)
saveButton.grid(column=0, row=6)



root.mainloop()