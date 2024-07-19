from transposer import *
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from chordprog import *
from view import *
from database import *
import customtkinter as ctk

battleship_gray = '#88958D'
ebony = '#606D5D'
french_gray = '#D3CDD7'
mint_green = '#DDF2EB'
tan = '#fff1d9'

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
        for widget in bottomFrame2.winfo_children():
            widget.destroy()

        lbl_cur_sel = ctk.CTkLabel(bottomFrame2, text="", font=('Roboto', 20, 'bold'), fg_color='#88958D')
        lbl_cur_sel.pack(pady=(20, 5))

        lbl_cur_key = ctk.CTkLabel(bottomFrame2, text="", font=('Roboto', 14, 'bold'), fg_color='#88958D')
        lbl_cur_key.pack(pady=5)

        lbl_cur_bpm = ctk.CTkLabel(bottomFrame2, text="", font=('Roboto', 14, 'bold'), fg_color='#88958D')
        lbl_cur_bpm.pack(pady=5)

        lbl_cur_ts = ctk.CTkLabel(bottomFrame2, text="", font=('Roboto', 14, 'bold'), fg_color='#88958D')
        lbl_cur_ts.pack(pady=5)

        lbl_cur_chords = ctk.CTkLabel(bottomFrame2, text="", font=('Roboto', 16, 'bold'), fg_color='#88958D')
        lbl_cur_chords.pack(pady=(5,20))

        frame_de = ctk.CTkFrame(bottomFrame2, width=100, height=20, fg_color='#88958D')    
        del_button = ctk.CTkButton(frame_de, text="Delete", width=50, fg_color='#DDF2EB', font=('Roboto', 16, 'bold'), 
                                text_color='black', hover_color='white', command=delete_clicked)
        edit_button = ctk.CTkButton(frame_de, text="Edit", width=50, fg_color='#DDF2EB', font=('Roboto', 16, 'bold'), 
                                    text_color='black', hover_color='white', command=edit)
        curSelection = lib_list.curselection()
        lbl_cur_sel.configure(text=lib_list.get(curSelection))
        
        tmp = df[df['Name'] == lib_list.get(curSelection)].index.values
        global curIndex
        curIndex = tmp[0]
        global origKey
        origKey = df['Key'][curIndex]
        txt_chords = df['Chords'][curIndex]
        txt_key = "Key: " + df['Key'][curIndex]
        txt_bpm = "BPM: " + str(df['BPM'][curIndex])
        txt_ts = "Time Signature: " + df['Time Signature'][curIndex]

        lbl_cur_chords.configure(text=txt_chords)
        lbl_cur_key.configure(text=txt_key)
        lbl_cur_bpm.configure(text=txt_bpm)
        lbl_cur_ts.configure(text=txt_ts)

        frame_de.pack(pady=(0,20))
        del_button.pack(side='left', padx=5)
        edit_button.pack(side='right', padx=5)
    
    def delete_clicked():
        cs = lib_list.curselection()
        curIndex = df[df['Name'] == lib_list.get(cs)].index.values
        print(curIndex[0])
        Delete(curIndex[0])
        lib_clicked()

    def edit():
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
            edit()

        curInd = curIndex
        curName = df['Name'][curInd]
        curChords = df['Chords'][curInd]
        curTime = df['Time Signature'][curInd]
        curKey = df['Key'][curInd]
        curBPM = int(df['BPM'][curInd])
        cur = ChordProgression(curName, curChords, curTime, curKey, curBPM)
        for widget in bottomFrame2.winfo_children():
            widget.destroy()

        edit_title = ctk.CTkLabel(bottomFrame2, text="Edit \"" + curName + "\"", font=('Roboto', 20, 'bold'), 
                                  fg_color='#88958D')
        edit_title.pack(pady=10)

        edit_name = ctk.CTkEntry(bottomFrame2, width=175, height=30, corner_radius=10, 
                                 font=('Roboto', 16))
        edit_name.insert(0, curName)
        edit_name.pack(pady=(0,10))

        keyFrame = ctk.CTkFrame(bottomFrame2, fg_color='#88958D')
        keyFrame.pack(pady=5)
        lbl_key = ctk.CTkLabel(keyFrame, text="Key: ", font=('Roboto', 14, 'bold'), fg_color='#88958D')
        lbl_key.pack(side='left', padx=2)
        keysCB = ctk.CTkComboBox(keyFrame, values=keys, state='normal', width=100, dropdown_fg_color='#fff1d9', 
                                 dropdown_font=('Roboto', 12, 'bold'), dropdown_hover_color='#D3CDD7', 
                                 font=('Roboto', 16, 'bold'), corner_radius=10, hover=True, button_color=ebony,  
                                 button_hover_color='white', command=key_change)
        keysCB.set(curKey)
        keysCB.pack(side='left', padx=2)

        def bpm_down_clicked():
            bpm_scale.set(bpm_scale.get() - 1)
            lbl_bpm.configure(text="BPM: " + str(int(bpm_scale.get())))

        def bpm_up_clicked():
            bpm_scale.set(bpm_scale.get() + 1)
            lbl_bpm.configure(text="BPM: " + str(int(bpm_scale.get())))

        def bpm_change(event):
            lbl_bpm.configure(text="BPM: " + str(int(bpm_scale.get())))

        bpmFrame = ctk.CTkFrame(bottomFrame2, fg_color=battleship_gray)
        lbl_bpm = ctk.CTkLabel(bottomFrame2, text="BPM: 100", font=('Roboto', 16, 'bold'), fg_color=battleship_gray)
        bpm_down = ctk.CTkButton(bpmFrame, text="<<", width=20, fg_color=ebony, hover_color='white', 
                                text_color='black', corner_radius=10, command=bpm_down_clicked)
        bpm_scale = ctk.CTkSlider(bpmFrame, from_=30, to=250, number_of_steps=220, button_color='black', 
                                button_hover_color='white', fg_color=mint_green, progress_color=mint_green, command=bpm_change)
        bpm_scale.set(curBPM)
        bpm_up = ctk.CTkButton(bpmFrame, text=">>", width=20, fg_color=ebony, hover_color='white', 
                            text_color='black', corner_radius=10, command=bpm_up_clicked)

        lbl_bpm.pack(pady=(5,0))
        bpmFrame.pack(pady=5)
        bpm_down.pack(side='left')
        bpm_scale.pack(side='left')
        bpm_up.pack(side='left')

        chordFrame = ctk.CTkFrame(bottomFrame2, width=110, height=160, fg_color=battleship_gray, corner_radius=10)
        chordFrame.pack(padx=5, pady=1)

        global chordProgCB
        chordProgCB = []
        i = 0
        if curTime == '4/4':
            for r in range(1, 5):
                curFrame = ctk.CTkFrame(chordFrame, fg_color=battleship_gray)
                curFrame.pack(pady=5, padx=5)
                for col in range(1, 5):
                    curCB = ctk.CTkComboBox(curFrame, values=chords, state='normal', width=70, dropdown_fg_color='#fff1d9', 
                                dropdown_font=('Roboto', 10, 'bold'), dropdown_hover_color='#D3CDD7', 
                                font=('Roboto', 12, 'bold'), corner_radius=10, hover=True, button_hover_color='white', button_color=ebony)
                    if curKey in flatKeys:
                        curCB.configure(values=chords_f)
                    else:
                        curCB.configure(values=chords_s)
                    while cur.chordProg[i] == '|':
                        i += 1
                    curCB.set(cur.chordProg[i])
                    i += 1
                    curCB.pack(side='left', padx=3)
                    chordProgCB.append(curCB)
        else:
            for r in range(1, 5):
                curFrame = ctk.CTkFrame(chordFrame, fg_color=battleship_gray)
                curFrame.pack(pady=5, padx=5)
                for col in range(1, 7):
                    curCB = ctk.CTkComboBox(curFrame, values=chords, state='normal', width=65, dropdown_fg_color='#fff1d9', 
                                dropdown_font=('Roboto', 10, 'bold'), dropdown_hover_color='#D3CDD7', 
                                font=('Roboto', 10, 'bold'), corner_radius=10, hover=True, button_hover_color='white', button_color=ebony)
                    if curKey in flatKeys:
                        curCB.configure(values=chords_f)
                    else:
                        curCB.configure(values=chords_s)
                    while cur.chordProg[i] == '|':
                        i += 1
                    curCB.set(cur.chordProg[i])
                    i += 1
                    curCB.pack(side='left', padx=1)
                    chordProgCB.append(curCB)

        def save_edit_clicked():
            if edit_name.get() == "":
                warningLabel.configure(text="Please Enter Name")
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
                cp = ChordProgression(edit_name.get(), cpStr, curTime, keysCB.get(), bpm_scale.get())
                df.loc[curIndex] = [edit_name.get(), keysCB.get(), bpm_scale.get(), curTime, cp.ToString()]
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

        buttonFrame = ctk.CTkFrame(bottomFrame2, fg_color=battleship_gray)
        buttonFrame.pack(pady=5)
        saveButton = ctk.CTkButton(buttonFrame, text="Save Changes", width=80, fg_color=mint_green, 
                                   hover_color='white', font=('Roboto', 14, 'bold'), text_color='black', command=save_edit_clicked)
        saveButton.pack(side='left', padx=2)
        cancelButton = ctk.CTkButton(buttonFrame, text="Cancel", width=80, fg_color=mint_green, 
                                   hover_color='white', font=('Roboto', 14, 'bold'), text_color='black', command=cancel_clicked)
        cancelButton.pack(side='left', padx=2)
        warningLabel = ctk.CTkLabel(bottomFrame2, text="", font=('Helvetica', 10), text_color='red')
        warningLabel.pack(pady=(5,10))
        
        
    # Library Screen
    clearWindow()
    topFrame = ctk.CTkFrame(root)
    topFrame.pack(fill='x')
    topFrame1 = ctk.CTkFrame(topFrame, width=500, fg_color='#606D5D')
    topFrame1.pack(fill='both', pady=(5, 2.5), padx=5)
    lib_title = ctk.CTkLabel(topFrame1, text="Library", font=('Roboto', 22, 'bold'), text_color='white', height=40)
    lib_title.pack()

    cp_names = []
    for ind in df.index:
        cp_names.append(df['Name'][ind])
    cp_names.sort()

    bottomFrame = ctk.CTkFrame(root)
    bottomFrame.pack(fill='both')
    bottomFrame1 = ctk.CTkFrame(bottomFrame, fg_color='#88958D', )
    bottomFrame1.pack(side='left', padx=5, pady=5, fill='y')

    scroll = ttk.Scrollbar(bottomFrame1)
    lib_list_var = tk.Variable(value=cp_names)
    lib_list = tk.Listbox(bottomFrame1, yscrollcommand=scroll.set, listvariable=lib_list_var, 
                          font=('Roboto', 14, 'bold'), bg='#DDF2EB', height=350, width=15)
    lib_list.bind('<Double-1>', doubleclick_lb)
    lib_list.pack(side='left', fill='y', padx=(20,0), pady=20)
    scroll.pack(side='left', padx=(5,10))

    bottomFrame2 = ctk.CTkFrame(bottomFrame, fg_color='#88958D', width=400)
    bottomFrame2.pack(side='left', padx=(0,5), pady=5, fill='both', expand=True)

    lbl_cur_sel = ctk.CTkLabel(bottomFrame2, text="", font=('Roboto', 20, 'bold'), fg_color='#88958D')
    lbl_cur_sel.pack(pady=(20, 5))

    lbl_cur_key = ctk.CTkLabel(bottomFrame2, text="", font=('Roboto', 14, 'bold'), fg_color='#88958D')
    lbl_cur_key.pack(pady=5)

    lbl_cur_bpm = ctk.CTkLabel(bottomFrame2, text="", font=('Roboto', 14, 'bold'), fg_color='#88958D')
    lbl_cur_bpm.pack(pady=5)

    lbl_cur_ts = ctk.CTkLabel(bottomFrame2, text="", font=('Roboto', 14, 'bold'), fg_color='#88958D')
    lbl_cur_ts.pack(pady=5)

    lbl_cur_chords = ctk.CTkLabel(bottomFrame2, text="", font=('Roboto', 16, 'bold'), fg_color='#88958D')
    lbl_cur_chords.pack(pady=(5,20))

    frame_de = ctk.CTkFrame(bottomFrame2, width=100, height=20, fg_color='#88958D')    
    del_button = ctk.CTkButton(frame_de, text="Delete", width=50, fg_color='#DDF2EB', font=('Roboto', 16, 'bold'), 
                               text_color='black', hover_color='white', command=delete_clicked)
    edit_button = ctk.CTkButton(frame_de, text="Edit", width=50, fg_color='#DDF2EB', font=('Roboto', 16, 'bold'), 
                                text_color='black', hover_color='white', command=edit)


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