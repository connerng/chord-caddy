
notes_s = ["G#", "A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G"]
notes_f = ["Ab", "A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G"]

def Transpose(chord: str, semitones: int, newSF: str, oldSF: str):
    new_chord = ""
    minor = False
    if 'm' in chord:
        minor = True
        chord = chord[0:len(chord)-1]
    if chord not in notes_s and chord not in notes_f:
        return "Err"
    
    if oldSF == "s":
        # old key uses sharps
        cur_index = notes_s.index(chord)
    else:
        # old key uses flats
        cur_index = notes_f.index(chord)
    if newSF == "s":
        # new key uses sharps
        if semitones > 0:
            for i in range(0, semitones):
                if cur_index == len(notes_s) - 1:
                    cur_index = 0
                else:
                    cur_index += 1
            new_chord = notes_s[cur_index]
        else:
            for i in range(0, abs(semitones)):
                if cur_index == 0:
                    cur_index = len(notes_s) - 1
                else:
                    cur_index -= 1
            new_chord = notes_s[cur_index]
    else:
        # new key uses flats
        if semitones > 0:
            for i in range(0, semitones):
                if cur_index == len(notes_f) - 1:
                    cur_index = 0
                else:
                    cur_index += 1
            new_chord = notes_f[cur_index]
        else:
            for i in range(0, abs(semitones)):
                if cur_index == 0:
                    cur_index = len(notes_f) - 1
                else:
                    cur_index -= 1
            new_chord = notes_f[cur_index]
    if minor:
        new_chord += "m"
    return new_chord


def TransposeKey(key: str, semitones: int):
    newKey = ""
    sf = ""
    if 'b' in key:
        sf = "f"
    if "#" in key:
        sf = "s"
    if sf == "f":
        cur_index = notes_f.index(key)
        if semitones > 0:
            for i in range(0, semitones):
                if cur_index == len(notes_f) - 1:
                    cur_index = 0
                else:
                    cur_index += 1
            newKey = notes_f[cur_index]
        else:
            for i in range(0, abs(semitones)):
                if cur_index == 0:
                    cur_index = len(notes_f) - 1
                else:
                    cur_index -= 1
            newKey = notes_f[cur_index]
    elif sf == "s":
        cur_index = notes_s.index(key)
        if semitones > 0:
            for i in range(0, semitones):
                if cur_index == len(notes_s) - 1:
                    cur_index = 0
                else:
                    cur_index += 1
            newKey = notes_s[cur_index]
        else:
            for i in range(0, abs(semitones)):
                if cur_index == 0:
                    cur_index = len(notes_s) - 1
                else:
                    cur_index -= 1
            newKey = notes_s[cur_index]
    else:
        if semitones > 0:
            cur_index = notes_s.index(key)
            for i in range(0, semitones):
                if cur_index == len(notes_s) - 1:
                    cur_index = 0
                else:
                    cur_index += 1
            newKey = notes_s[cur_index]
        else:
            cur_index = notes_f.index(key)
            for i in range(0, abs(semitones)):
                if cur_index == 0:
                    cur_index = len(notes_f) - 1
                else:
                    cur_index -= 1
            newKey = notes_f[cur_index]
    return newKey