from transposer import *
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from chordprog import *
from view import *
from database import *

chords = ['.','Ab', 'Abm', 'A', 'Am', 'A#', 'A#m', 'Bb', 'Bbm', 'B', 'Bm', 'C', 'Cm', 'C#', 'C#m', 'Db', 'Dbm', 
          'D', 'Dm', 'D#', 'D#m', 'Eb', 'Ebm', 'E', 'Em', 'F', 'Fm', 'F#', 'F#m', 'Gb', 'Gbm', 'G', 'Gm', 
          'G#', 'G#m']

keys = ['.', 'Ab', 'A', 'A#', 'Bb', 'B', 'C', 'C#', 'Db', 'D', 'D#', 'Eb', 'E', 'F', 'F#', 'Gb', 'G', 'G#']


def show(widget):
    widget.pack()

def hide(widget):
    widget.pack_forget()


def ts_44_clicked():
    create_new_clicked()
    global timeSignature
    timeSignature = "4/4"
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
    global timeSignature
    timeSignature = "6/8"
    global chordProgCB
    chordProgCB = []
    for r in range(1, 5):
        for col in range(1, 7):
            cur = ttk.Combobox(root, values=chords, state='readonly', width=5)
            cur.current(0)
            cur.place(x = (col * 50) + 50, y = (r * 25) + 60)
            chordProgCB.append(cur)

def create_new_clicked():

    def save_clicked():
        cpStr = "|"
        for i in range(0, len(chordProgCB)):
            cpStr += chordProgCB[i].get()
            if timeSignature == "4/4":
                if (i+1)%4 == 0:
                    cpStr += "|"
            else:
                if (i+1)%6 == 0:
                    cpStr += "|"
        cp = ChordProgression(cp_name_entry.get(), cpStr, timeSignature, keysCB.get(), bpm_scale.get())
        AddNew(cp)
        create_new_clicked()


    clearWindow()
    keysList = keys
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

    bpm_scale = tk.Scale(root, from_=30, to=250, orient='horizontal', length=300, label="BPM")
    bpm_scale.set(100)
    bpm_scale.place(x=100, y=250)


    saveButton = ttk.Button(root, text="Save", width=10, command=save_clicked)
    saveButton.place(x=215, y=320)


def play_clicked():
    print("Play")

def lib_clicked():

    def doubleclick_lb(event):
        cs = lib_list.curselection()
        lbl_cur_sel.config(text=lib_list.get(cs))
        
        curIndex = df[df['Name'] == lib_list.get(cs)].index.values
        txt_chords = df['Chords'][curIndex[0]]
        txt_key = "Key: " + df['Key'][curIndex[0]]
        txt_bpm = "BPM: " + str(df['BPM'][curIndex[0]])
        txt_ts = "Time Signature: " + df['Time Signature'][curIndex[0]]

        lbl_cur_chords.config(text=txt_chords)
        lbl_cur_key.config(text=txt_key)
        lbl_cur_bpm.config(text=txt_bpm)
        lbl_cur_ts.config(text=txt_ts)

        frame_de.pack(pady=5)
        del_button.pack(side='left')
        edit_button.pack(side='right')
    
    def delete_clicked():
        cs = lib_list.curselection()
        curIndex = df[df['Name'] == lib_list.get(cs)].index.values
        Delete(curIndex[0])
        lib_clicked()


    def edit_clicked():
        cs = lib_list.curselection()

        frame_name = ttk.Frame(root, width=100, height=20)
        frame_name.pack(pady=5)
        name_entry = ttk.Entry(frame_name)
        name_entry.insert(0, lib_list.get(cs))
        name_entry.pack(side='right')
        lbl_name_entry = ttk.Label(frame_name, text="Name: ", font=('Helvetica', 10), background='light yellow')
        lbl_name_entry.pack(side='left')

        frame_key_ts = ttk.Frame(root, width=100, height=20)
        frame_key_ts.pack(pady=5)
        lbl_key_entry = ttk.Label(frame_key_ts, text="Key: ", font=('Helvetica', 10), background='light yellow')
        lbl_key_entry.pack(side='left')
        key_entry = ttk.Combobox(frame_key_ts, values=keys, state='readonly', width=5)
        key_entry.current(0)
        key_entry.pack(side='left')
        lbl_ts_entry = ttk.Label(frame_key_ts, text="Time Signature: ", font=('Helvetica', 10), background='light yellow')
        lbl_ts_entry.pack(side='left', padx=(10, 0))
        


        
        

    clearWindow()
    lib_title = ttk.Label(root, text="Library", font=('Helvetica', 14), background='light yellow')
    lib_title.pack()

    cp_names = []
    for ind in df.index:
        cp_names.append(df['Name'][ind])
    cp_names.sort()

    scroll = ttk.Scrollbar(root)
    lib_list_var = tk.Variable(value=cp_names)
    lib_list = tk.Listbox(root, yscrollcommand=scroll.set, listvariable=lib_list_var)
    lib_list.bind('<Double-1>', doubleclick_lb)
    lib_list.pack(side='left', fill='y', padx=(20,0), pady=20)
    scroll.pack(side='left')

    lbl_cur_sel = ttk.Label(root, text="Name", font=('Helvetica', 12, 'bold'), background='light yellow')
    lbl_cur_sel.pack(pady=(20, 5))

    lbl_cur_key = ttk.Label(root, text="Key: ", font=('Helvetica', 12), background='light yellow')
    lbl_cur_key.pack(pady=5)

    lbl_cur_bpm = ttk.Label(root, text="BPM: ", font=('Helvetica', 12), background='light yellow')
    lbl_cur_bpm.pack(pady=5)

    lbl_cur_ts = ttk.Label(root, text="Time Signature:", font=('Helvetica', 12), background='light yellow')
    lbl_cur_ts.pack(pady=5)

    lbl_cur_chords = ttk.Label(root, text="| | | |", font=('Helvetica', 12), background='light yellow')
    lbl_cur_chords.pack(pady=5)

    frame_de = ttk.Frame(root, width=100, height=20)    
    del_button = ttk.Button(frame_de, text="Delete", width=10, command=delete_clicked)
    edit_button = ttk.Button(frame_de, text="Edit", width=10, command=edit_clicked)



root = tk.Tk()
root.title("Chord Caddy")
root.geometry('500x400')
root['bg'] = 'light yellow'

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