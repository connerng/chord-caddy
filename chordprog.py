from transposer import *
from typing import List

flatKeys = ["C", "F", "Bb", "Eb", "Ab", "Db", "Gb"]
sharpKeys = ["C", "G", "D", "A", "E", "B", "F#", "C#", "G#", "D#", "A#"]

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
    if newKey in flatKeys:
        newSF = "f"
    else:
        newSF = "s"
    for item in cp.chordProg:
        if item[0].isalpha():
            cpStr += Transpose(item, semitones, newSF)
        else:
            cpStr += item
    newProg = ChordProgression(cpStr, cp.timeSig, newKey)
    return newProg


