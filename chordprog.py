from transposer import *
from typing import List

class ChordProgression:
    chordProg: List[str] = []
    timeSig = ""
    key = ""
    
    def __init__(self, cp_str: str, timeSig: str, key: str):
        cur = ""
        for c in cp_str:
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

    def TransposeCP(self, semitones: int):
        self.key = Transpose(self.key, semitones)
        for i in range(0, len(self.chordProg)):
            curItem = self.chordProg[i]
            if curItem[0].isalpha():
                self.chordProg[i] = Transpose(curItem, semitones)
        
        


