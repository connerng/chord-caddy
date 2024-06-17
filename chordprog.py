from transposer import *

class ChordProgression:
    def __init__(self, timeSig, key, chordProg):
        self.timeSig = timeSig
        self.key = key
        self.chordProg = chordProg
    
    def ToString(self):
        return self.chordProg
    
    def TransposeCP(self, semitones):
        i = 0
        cp_str = ""
        while i < len(self.chordProg):
            cur = self.chordProg[i:self.chordProg.find(' ', i)]
            i = self.chordProg.find(' ', i) + 1
            if cur[0] in notes_f:
                cp_str += Transpose(cur, semitones)
            else:
                cp_str += cur
        newKey = Transpose(self.key, semitones)
        return ChordProgression(self.timeSig, newKey, cp_str)



    
