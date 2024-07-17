import tkinter as tk
from tkinter import ttk

def create_new_clicked():

    def ts_44_clicked():
        create_new_clicked()
        global timeSignature
        timeSignature = "4/4"
        global chordProgCB
        chordProgCB = []

        for r in range(1, 5):
            curFrame = tk.Frame(root, bg='light yellow')
            curFrame.pack(pady=3)
            for col in range(1, 5):
                cur = ttk.Combobox(curFrame, values=chords, state='readonly', width=5)
                cur.current(0)
                cur.pack(side='left', padx=1)
                chordProgCB.append(cur)

    def ts_68_clicked():
        create_new_clicked()
        global timeSignature
        timeSignature = "6/8"
        global chordProgCB
        chordProgCB = []

        for r in range(1, 5):
            curFrame = tk.Frame(root, bg='light yellow')
            curFrame.pack(pady=3)
            for col in range(1, 7):
                cur = ttk.Combobox(curFrame, values=chords, state='readonly', width=5)
                cur.current(0)
                cur.pack(side='left', padx=1)
                chordProgCB.append(cur)

    def save_clicked():
        if cp_name_entry.get() == "":
            warningLabel.config(text="Please Enter Name")
        elif keysCB.get() == '.':
            warningLabel.config(text="Please Select Key")
        elif 'chordProg' not in globals():
            warningLabel.config(text="Error: No Chords")
        else:
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
            lib_clicked()
    
    def bpm_down_clicked():
        bpm_scale.set(bpm_scale.get() - 1)

    def bpm_up_clicked():
        bpm_scale.set(bpm_scale.get() + 1)

    clearWindow()
    keysList = keys
    topFrame = ctk.CTkFrame(root, width = 500, height = 50, fg_color='#98e7ff')
    topFrame.pack()
    new_cp_title = ctk.CTkLabel(topFrame, text="Create New Chord Progression", font=('Segoe Print', 20, 'bold'), corner_radius=0)
    new_cp_title.pack(pady=10, padx=95)

    nameFrame = tk.Frame(root, bg='light yellow')
    lbl_cpname = ttk.Label(nameFrame, text="Name: ", font=('Helvetica', 10), background='light yellow')
    cp_name_entry = ttk.Entry(nameFrame)

    keyFrame = tk.Frame(root, bg='light yellow')
    lbl_key = ttk.Label(keyFrame, text="Key: ", font=('Helvetica', 10), background='light yellow')
    keysCB = ttk.Combobox(keyFrame, values=keysList, state='readonly', width=5)
    keysCB.current(0)

    bpmFrame = tk.Frame(root, bg='light yellow')
    bpm_down = ttk.Button(bpmFrame, text="<<", width=3, command=bpm_down_clicked)
    bpm_scale = tk.Scale(bpmFrame, from_=30, to=250, orient='horizontal', length=300, label="BPM")
    bpm_scale.set(100)
    bpm_up = ttk.Button(bpmFrame, text=">>", width=3, command=bpm_up_clicked)

    timeSigFrame = tk.Frame(root, bg='light yellow')
    lbl_timeSig = ttk.Label(timeSigFrame, text="Time Signature:", font=('Helvetica', 10), background='light yellow')
    ts_44_button = ttk.Button(timeSigFrame, text="4/4", width=10, command=ts_44_clicked)
    ts_68_button = ttk.Button(timeSigFrame, text="6/8", width=10, command=ts_68_clicked)

    nameFrame.pack(pady=5)
    lbl_cpname.pack(side='left', padx=(0,2))
    cp_name_entry.pack(side='left', padx=2)

    keyFrame.pack(pady=5)
    lbl_key.pack(side='left', padx=(0,2))
    keysCB.pack(side='left', padx=2)

    bpmFrame.pack(pady=5)
    bpm_down.pack(side='left', padx=(0,2))
    bpm_scale.pack(side='left', padx=2)
    bpm_up.pack(side='left', padx=2)

    timeSigFrame.pack(pady=5)
    lbl_timeSig.pack(side='left', padx=(0,2))
    ts_44_button.pack(side='left', padx=2)
    ts_68_button.pack(side='left', padx=2)
    
    saveButton = ttk.Button(root, text="Save", width=10, command=save_clicked)
    warningLabel = ttk.Label(root, text="", font=('Helvetica', 10), background='light yellow')
    saveButton.place(x=215, y=305)
    warningLabel.place(x=195, y=340)