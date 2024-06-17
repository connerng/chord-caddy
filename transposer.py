
notes_s = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
notes_f = ["Ab", "A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G"]

def Transpose(chord, semitones):
    new_chord = ""
    minor = False
    if 'm' in chord:
        minor = True
        chord = chord[0:len(chord)-1]
    if chord not in notes_s and chord not in notes_f:
        return "Err"
    if '#' in chord:
        # chord is a sharp
        cur_index = notes_s.index(chord)
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
        # chord is a flat or natural
        cur_index = notes_f.index(chord)
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
