from transposer import *
from typing import List

class ChordProgression:
    chordProg: List[str] = []
    timeSig = ""
    key = ""
    
    def __init__(self, cpStr: str, timeSig: str, key: str):
        cur = ""
        self.chordProg = []
        for c in cpStr:
            if c.isalpha():
                cur += c
            else:
                if len(cur) > 0:
                    self.chordProg.append(cur)
                cur = ""
                self.chordProg.append(c)
        self.key = key
        self.timeSig = timeSig

    def __str__(self):
        retVal = self.chordProg[0]
        for i in range(1, len(self.chordProg)):
            retVal += " " + self.chordProg[i]
        return retVal


def TransposeCP(cp: ChordProgression, semitones: int):
    cpStr = ""
    newKey = Transpose(cp.key, semitones)
    for item in cp.chordProg:
        if item[0].isalpha():
            cpStr += Transpose(item, semitones)
        else:
            cpStr += item
    newProg = ChordProgression(cpStr, cp.timeSig, newKey)
    return newProg

        
        


