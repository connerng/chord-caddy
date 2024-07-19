from transposer import *
from typing import List

flatKeys = ["C", "F", "Bb", "Eb", "Ab", "Db", "Gb"]
sharpKeys = ["G", "D", "A", "E", "B", "F#", "C#", "G#", "D#", "A#"]
chords = ['.','Ab', 'Abm', 'A', 'Am', 'A#', 'A#m', 'Bb', 'Bbm', 'B', 'Bm', 'C', 'Cm', 'C#', 'C#m', 'Db', 'Dbm', 
          'D', 'Dm', 'D#', 'D#m', 'Eb', 'Ebm', 'E', 'Em', 'F', 'Fm', 'F#', 'F#m', 'Gb', 'Gbm', 'G', 'Gm', 
          'G#', 'G#m']
chords_f= ['.','Ab', 'Abm', 'A', 'Am', 'Bb', 'Bbm', 'B', 'Bm', 'C', 'Cm', 'Db', 'Dbm', 'D', 'Dm', 'Eb', 'Ebm', 
           'E', 'Em', 'F', 'Fm', 'Gb', 'Gbm', 'G', 'Gm']
chords_s = ['.', 'A', 'Am', 'A#', 'A#m', 'B', 'Bm', 'C', 'Cm', 'C#', 'C#m', 'D', 'Dm', 'D#', 'D#m', 'E', 'Em', 
            'F', 'Fm', 'F#', 'F#m', 'G', 'Gm', 'G#', 'G#m']

keys = ['(Key)', 'Ab', 'A', 'A#', 'Bb', 'B', 'C', 'C#', 'Db', 'D', 'D#', 'Eb', 'E', 'F', 'F#', 'Gb', 'G', 'G#']

class ChordProgression:
    chordProg: List[str] = []
    timeSig = ""
    key = ""
    scale = []
    sf = ""
    bpm = 0
    name = ""
    
    def __init__(self, name: str, cpStr: str, timeSig: str, key: str, bpm: int):
        cur = ""
        self.chordProg = []
        for c in cpStr:
            if c.isalpha() or c == '#':
                cur += c
            else:
                if len(cur) > 0:
                    self.chordProg.append(cur)
                cur = ""
                if c != " ":
                    self.chordProg.append(c)
        if len(cur) > 0:
            self.chordProg.append(cur)
        self.key = key
        self.timeSig = timeSig
        self.bpm = bpm
        self.name = name
        if key in flatKeys:
            sf = "f"
        else:
            sf = "s"
        

    def __str__(self):
        retVal = self.chordProg[0]
        for i in range(1, len(self.chordProg)):
            retVal += " " + self.chordProg[i]
        return retVal
    
    def ToString(self):
        retVal = self.chordProg[0]
        for i in range(1, len(self.chordProg)):
            retVal += " " + self.chordProg[i]
        return retVal


def TransposeCP(cp: ChordProgression, semitones: int):
    cpStr = ""
    newKey = TransposeKey(cp.key, semitones)
    if cp.key in flatKeys:
        oldSF = "f"
    else:
        oldSF = "s"
    if newKey in flatKeys:
        newSF = "f"
    else:
        newSF = "s"
    for item in cp.chordProg:
        if item[0].isalpha():
            cpStr += Transpose(item, semitones, newSF, oldSF)
        else:
            cpStr += item
    newProg = ChordProgression(cp.name, cpStr, cp.timeSig, newKey, cp.bpm)
    return newProg

