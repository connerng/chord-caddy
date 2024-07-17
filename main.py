from transposer import *
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from chordprog import *
from view import *
from database import *
import customtkinter as ctk

chords = ['.','Ab', 'Abm', 'A', 'Am', 'A#', 'A#m', 'Bb', 'Bbm', 'B', 'Bm', 'C', 'Cm', 'C#', 'C#m', 'Db', 'Dbm', 
          'D', 'Dm', 'D#', 'D#m', 'Eb', 'Ebm', 'E', 'Em', 'F', 'Fm', 'F#', 'F#m', 'Gb', 'Gbm', 'G', 'Gm', 
          'G#', 'G#m']
chords_f= ['.','Ab', 'Abm', 'A', 'Am', 'Bb', 'Bbm', 'B', 'Bm', 'C', 'Cm', 'Db', 'Dbm', 'D', 'Dm', 'Eb', 'Ebm', 
           'E', 'Em', 'F', 'Fm', 'Gb', 'Gbm', 'G', 'Gm']
chords_s = ['.', 'A', 'Am', 'A#', 'A#m', 'B', 'Bm', 'C', 'Cm', 'C#', 'C#m', 'D', 'Dm', 'D#', 'D#m', 'E', 'Em', 
            'F', 'Fm', 'F#', 'F#m', 'G', 'Gm', 'G#', 'G#m']

keys = ['(Key)', 'Ab', 'A', 'A#', 'Bb', 'B', 'C', 'C#', 'Db', 'D', 'D#', 'Eb', 'E', 'F', 'F#', 'Gb', 'G', 'G#']

root = ctk.CTk()
root.title("Chord Caddy")
root.geometry('600x500')

style = ttk.Style()
style.theme_use('vista')


def create_new_clicked():

    def ts_44_clicked():
        for widget in chordFrame.winfo_children():
            widget.destroy()
        global timeSignature
        timeSignature = "4/4"
        global chordProgCB
        chordProgCB = []

        for r in range(1, 5):
            curFrame = ctk.CTkFrame(chordFrame, fg_color='#606D5D')
            curFrame.pack(pady=5, padx=5)
            for col in range(1, 5):
                cur = ctk.CTkComboBox(curFrame, values=chords, state='normal', width=80, dropdown_fg_color='#fff1d9', 
                             dropdown_font=('Roboto', 10, 'bold'), dropdown_hover_color='#D3CDD7', 
                             font=('Roboto', 16, 'bold'), corner_radius=10, hover=True, button_hover_color='white')
                if keysCB.get() in flatKeys:
                    cur.configure(values=chords_f)
                    cur.set(chords_f[0])
                elif keysCB.get() in sharpKeys:
                    cur.configure(values=chords_s)
                    cur.set(chords_s[0])
                else:
                    cur.set(chords[0])
                cur.pack(side='left', padx=3)
                chordProgCB.append(cur)

    def ts_68_clicked():
        for widget in chordFrame.winfo_children():
            widget.destroy()
        global timeSignature
        timeSignature = "6/8"
        global chordProgCB
        chordProgCB = []

        for r in range(1, 5):
            curFrame = ctk.CTkFrame(chordFrame, fg_color='#606D5D')
            curFrame.pack(pady=5, padx=5)
            for col in range(1, 7):
                cur = ctk.CTkComboBox(curFrame, values=chords, state='normal', width=80, dropdown_fg_color='#fff1d9', 
                             dropdown_font=('Roboto', 10, 'bold'), dropdown_hover_color='#D3CDD7', 
                             font=('Roboto', 16, 'bold'), corner_radius=10, hover=True, button_hover_color='white')
                if keysCB.get() in flatKeys:
                    cur.configure(values=chords_f)
                    cur.set(chords_f[0])
                elif keysCB.get() in sharpKeys:
                    cur.configure(values=chords_s)
                    cur.set(chords_s[0])
                else:
                    cur.set(chords[0])
                cur.pack(side='left', padx=3)
                chordProgCB.append(cur)

    def save_clicked():
        if cp_name_entry.get() == "":
            warningLabel.configure(text="Please Enter Name")
        elif keysCB.get() == '.':
            warningLabel.configure(text="Please Select Key")
        elif 'chordProgCB' not in globals():
            warningLabel.configure(text="Error: No Chords")
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
        lbl_bpm.configure(text="BPM: " + str(int(bpm_scale.get())))

    def bpm_up_clicked():
        bpm_scale.set(bpm_scale.get() + 1)
        lbl_bpm.configure(text="BPM: " + str(int(bpm_scale.get())))

    def bpm_change(event):
        lbl_bpm.configure(text="BPM: " + str(int(bpm_scale.get())))

    def key_select(event):
        if 'chordProgCB' in globals():
            curKey = keysCB.get()
            for cb in chordProgCB:
                if curKey in flatKeys:
                    cb.configure(values=chords_f)
                else:
                    cb.configure(values=chords_s)

    clearWindow()
    keysList = keys
    topFrame = ctk.CTkFrame(root)
    topFrame.pack(fill='x')
    topFrame1 = ctk.CTkFrame(topFrame, width=500, height=75, fg_color='#606D5D')
    topFrame1.pack(fill='x', pady=(5, 2.5), padx=5)
    new_cp_title = ctk.CTkLabel(topFrame1, text="Create New Chord Progression", font=('Roboto', 22, 'bold'), text_color='white')
    new_cp_title.pack(pady=10)

    middleFrame = ctk.CTkFrame(root, fg_color='#D3CDD7')
    middleFrame.pack(fill='x')
    midFrame1 = ctk.CTkFrame(middleFrame, width=292.5, height= 175, fg_color='#DDF2EB')
    midFrame1.pack(side='left', padx=(5,2.5), pady=5, fill='both', expand=True)
    midFrame2 = ctk.CTkFrame(middleFrame, width=292.5, height=175, fg_color='#DDF2EB')
    midFrame2.pack(side='left', padx=(2.5,5), pady=5, fill='both', expand=True)

    bottomFrame = ctk.CTkFrame(root, fg_color='#D3CDD7')
    bottomFrame.pack(fill='both')
    bottomFrame1 = ctk.CTkFrame(bottomFrame, width=590, height=300, fg_color='#88958D')
    bottomFrame1.pack(padx=5, pady=(0,5), fill='both')
    bottomFrame2 = ctk.CTkFrame(bottomFrame, fg_color='gray')
    bottomFrame2.pack(side='bottom', padx=5, pady=(0,5), fill='both')

    cp_name_entry = ctk.CTkEntry(midFrame1, width=175, height=30, corner_radius=10, font=('Roboto', 16), placeholder_text="Enter Name")
    cp_name_entry.pack(pady=(20,10))

    keysCB = ctk.CTkComboBox(midFrame1, values=keysList, state='normal', width=100, dropdown_fg_color='#fff1d9', 
                             dropdown_font=('Roboto', 12, 'bold'), dropdown_hover_color='#D3CDD7', 
                             font=('Roboto', 16, 'bold'), corner_radius=10, hover=True, button_hover_color='white', command=key_select)
    keysCB.set(keysList[0])
    keysCB.pack(pady=(10,20))

    bpmFrame = ctk.CTkFrame(midFrame2, fg_color='#DDF2EB')
    lbl_bpm = ctk.CTkLabel(midFrame2, text="BPM: 100", font=('Roboto', 16, 'bold'), fg_color='#DDF2EB')
    bpm_down = ctk.CTkButton(bpmFrame, text="<<", width=20, fg_color='#88958D', hover_color='white', 
                             text_color='black', corner_radius=10, command=bpm_down_clicked)
    bpm_scale = ctk.CTkSlider(bpmFrame, from_=30, to=250, number_of_steps=220, button_color='black', 
                              button_hover_color='white', command=bpm_change)
    bpm_scale.set(100)
    bpm_up = ctk.CTkButton(bpmFrame, text=">>", width=20, fg_color='#88958D', hover_color='white', 
                           text_color='black', corner_radius=10, command=bpm_up_clicked)

    lbl_bpm.pack(pady=(20, 0))
    bpmFrame.pack(pady=5)
    bpm_down.pack(side='left')
    bpm_scale.pack(side='left')
    bpm_up.pack(side='left')

    timeSigFrame = ctk.CTkFrame(bottomFrame1, width=110, fg_color='#88958D')
    ts_44_button = ctk.CTkButton(timeSigFrame, text="4/4", width=100, text_color='black', border_color='white', 
                                 border_width=2, hover_color='white', fg_color='#DDF2EB', font=('Roboto', 16, 'bold'), 
                                 command=ts_44_clicked)
    ts_68_button = ctk.CTkButton(timeSigFrame, text="6/8", width=100, text_color='black', border_color='white', 
                                 border_width=2, hover_color='white', fg_color='#DDF2EB', font=('Roboto', 16, 'bold'),
                                 command=ts_68_clicked)

    timeSigFrame.pack(pady=10)
    ts_44_button.pack(side='left', padx=5)
    ts_68_button.pack(side='left', padx=5)

    chordFrame = ctk.CTkFrame(bottomFrame1, width=110, height=160, fg_color='#606D5D', corner_radius=10)
    chordFrame.pack(pady=(0,10))

    saveButton = ctk.CTkButton(bottomFrame2, text="Save", text_color='black', hover_color='white', width=100, 
                               fg_color='#DDF2EB', corner_radius=10, font=('Roboto', 16, 'bold'), command=save_clicked)
    saveButton.pack(pady=10)
    warningLabel = ctk.CTkLabel(bottomFrame2, text="", text_color='red', font=('Roboto', 12), fg_color='gray')
    warningLabel.pack(pady=(0,10))


def play_clicked():
    print("Play")

def lib_clicked():

    def doubleclick_lb(event):
        curSelection = lib_list.curselection()
        lbl_cur_sel.config(text=lib_list.get(curSelection))
        
        tmp = df[df['Name'] == lib_list.get(curSelection)].index.values
        global curIndex
        curIndex = tmp[0]
        global origKey
        origKey = df['Key'][curIndex]
        txt_chords = df['Chords'][curIndex]
        txt_key = "Key: " + df['Key'][curIndex]
        txt_bpm = "BPM: " + str(df['BPM'][curIndex])
        txt_ts = "Time Signature: " + df['Time Signature'][curIndex]

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
        def ts_44():
            global chordProgCB
            chordProgCB = []
            i = 0
            for r in range(1, 5):
                curFrame = tk.Frame(root, bg='light yellow')
                curFrame.pack(pady=3)
                for col in range(1, 5):
                    curCB = ttk.Combobox(curFrame, values=chords, state='readonly', width=5)
                    while cur.chordProg[i] == '|':
                        i += 1
                    curCB.current(chords.index(cur.chordProg[i]))
                    i += 1
                    curCB.pack(side='left', padx=1)
                    chordProgCB.append(curCB)
    

        def ts_68():
            global chordProgCB
            chordProgCB = []
            i = 0
            for r in range(1, 5):
                curFrame = tk.Frame(root, bg='light yellow')
                curFrame.pack(pady=3)
                for col in range(1, 7):
                    curCB = ttk.Combobox(curFrame, values=chords, state='readonly', width=5)
                    while cur.chordProg[i] == '|':
                        i += 1
                    curCB.current(chords.index(cur.chordProg[i]))
                    i += 1
                    curCB.pack(side='left', padx=1)
                    chordProgCB.append(curCB)

        def save_edit_clicked():
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
                    if curTime == "4/4":
                        if (i+1)%4 == 0:
                            cpStr += "|"
                    else:
                        if (i+1)%6 == 0:
                            cpStr += "|"
                cp = ChordProgression(cp_name_entry.get(), cpStr, curTime, keysCB.get(), bpm_scale.get())
                df.loc[curIndex] = [cp_name_entry.get(), keysCB.get(), bpm_scale.get(), curTime, cp.ToString()]
                print(df)
                Save()
                lib_clicked()
        
        def cancel_clicked():
            keysCB.set(origKey)
            newKey = keysCB.get()
            if curKey in flatKeys:
                indexOld = notes_f.index(curKey)
            else:
                indexOld = notes_s.index(curKey)
            if newKey in flatKeys:
                indexNew = notes_f.index(newKey)
            else:
                indexNew = notes_s.index(newKey)
            semitones = indexNew - indexOld
            transposed = TransposeCP(cur, semitones)
            df.loc[curIndex] = [transposed.name, transposed.key, transposed.bpm, transposed.timeSig, transposed.ToString()]
            print(df)
            lib_clicked()
        
        def key_change(event):
            newKey = keysCB.get()
            if curKey in flatKeys:
                indexOld = notes_f.index(curKey)
            else:
                indexOld = notes_s.index(curKey)
            if newKey in flatKeys:
                indexNew = notes_f.index(newKey)
            else:
                indexNew = notes_s.index(newKey)
            semitones = indexNew - indexOld
            transposed = TransposeCP(cur, semitones)
            df.loc[curIndex] = [transposed.name, transposed.key, transposed.bpm, transposed.timeSig, transposed.ToString()]
            print(df)
            edit_clicked()
        
        def bpm_down_clicked():
            bpm_scale.set(bpm_scale.get() - 1)

        def bpm_up_clicked():
            bpm_scale.set(bpm_scale.get() + 1)

        curInd = curIndex
        curName = df['Name'][curInd]
        curChords = df['Chords'][curInd]
        curTime = df['Time Signature'][curInd]
        curKey = df['Key'][curInd]
        curBPM = int(df['BPM'][curInd])
        cur = ChordProgression(curName, curChords, curTime, curKey, curBPM)
        
        clearWindow()
        edit_title = ttk.Label(root, text="Edit \"" + curName + "\"", font=('Helvetica', 14), background='light yellow')
        edit_title.pack()

        nameFrame = tk.Frame(root, bg='light yellow')
        nameFrame.pack(pady=5)
        lbl_cpname = ttk.Label(nameFrame, text="Name: ", font=('Helvetica', 10), background='light yellow')
        lbl_cpname.pack(side='left', padx=2)
        cp_name_entry = ttk.Entry(nameFrame)
        cp_name_entry.insert(0, curName)
        cp_name_entry.pack(side='left', padx=2)

        keyFrame = tk.Frame(root, bg='light yellow')
        keyFrame.pack(pady=5)
        lbl_key = ttk.Label(keyFrame, text="Key: ", font=('Helvetica', 10), background='light yellow')
        lbl_key.pack(side='left', padx=2)
        keysCB = ttk.Combobox(keyFrame, values=keys, state='readonly', width=5)
        keysCB.current(keys.index(curKey))
        keysCB.bind("<<ComboboxSelected>>", key_change)
        keysCB.pack(side='left', padx=2)


        bpmFrame = tk.Frame(root, bg='light yellow')
        bpmFrame.pack(pady=5)
        bpm_down = ttk.Button(bpmFrame, text="<<", width=3, command=bpm_down_clicked)
        bpm_down.pack(side='left', padx=2)
        bpm_scale = tk.Scale(bpmFrame, from_=30, to=250, orient='horizontal', length=300, label="BPM")
        bpm_scale.set(curBPM)
        bpm_scale.pack(side='left', padx=2)
        bpm_up = ttk.Button(bpmFrame, text=">>", width=3, command=bpm_up_clicked)
        bpm_up.pack(side='left', padx=2)

        lbl_timeSig = ttk.Label(root, text="Time Signature: " + curTime, font=('Helvetica', 10), background='light yellow')
        lbl_timeSig.pack(pady=10)

        if curTime == "4/4":
            ts_44()
        else:
            ts_68()

        for i in range(0, len(chordProgCB)):
            cb = ttk.Combobox(chordProgCB[i])
            index = 0
            if cur.chordProg[index] == '|':
                index += 1
            else:
                cb.current(chords.index(cur.chordProg[index]))

        buttonFrame = tk.Frame(root, bg='light yellow')
        buttonFrame.pack(pady=5)
        saveButton = ttk.Button(buttonFrame, text="Save Changes", width=15, command=save_edit_clicked)
        saveButton.pack(side='left', padx=2)
        cancelButton = ttk.Button(buttonFrame, text="Cancel", width=15, command=cancel_clicked)
        cancelButton.pack(side='left', padx=2)
        warningLabel = ttk.Label(root, text="", font=('Helvetica', 10), background='light yellow')
        warningLabel.pack(pady=10)
        
        
    # Library Screen
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