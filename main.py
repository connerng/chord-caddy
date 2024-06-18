from transposer import *
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from chordprog import *

# test_cp_str = "|C...|Am...|G...|F...|"
# test_str_2 = "|Am...|C...|Em...|D...|"
# cp = ChordProgression(test_cp_str, "4/4", "C")
# print(cp.timeSig)
# print(cp.key)
# print(cp)

# cp2 = ChordProgression(test_str_2, "4/4", "G")
# print(cp2.timeSig)
# print(cp2.key)
# print(cp2)

# cp3 = TransposeCP(cp, 1)
# print(cp3.timeSig)
# print(cp3.key)
# print(cp3)

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



timeSig = tk.StringVar()
timeSigs = ttk.Combobox(root, values=('4/4', '6/8'), state='readonly', width=4, textvariable=timeSig)
timeSigs.grid(column=1, row=0)
key = tk.StringVar()
keys = ttk.Combobox(root, values=keys, state='readonly', width=4, textvariable=key)
keys.grid(column=1,row=1)

chordProgCB = []
for r in range(2, 6):
    for col in range(1, 5):
        cur = ttk.Combobox(root, values=chords, state='readonly', width=4)
        cur.current(0)
        cur.grid(column=col, row=r)
        chordProgCB.append(cur)



def clicked():
    cpStr = "|"
    for i in range(0, len(chordProgCB)):
        cpStr += chordProgCB[i].get()
        if (i+1)%4 == 0:
            cpStr += "|"
    cp = ChordProgression(cpStr, timeSig.get(), key.get())
    showinfo(title="New Chord Progression", message=cp.ToString())

saveButton = ttk.Button(root, text="Save", width=50, command=clicked)
saveButton.grid(column=0, row=6)



root.mainloop()