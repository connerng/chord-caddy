from transposer import *

class ChordProgression:
    chordProg = []
    timeSig = ""
    key = ""
    
    def __init__(self, cp_str, timeSig, key):
        i = 0
        cp_str = ""
        skip = 0
        for i in range(0, len(cp_str)):
            if skip > 0:
                cur = cp_str[i]
                if cur.isalpha():
                    alpha = True
                    while alpha:
                        if cp_str[i+1].isalpha():
                            cur += cp_str[i+1]
                            i += 1
                            skip += 1
                        else:
                            i += 1
                            print('nonletter at ', i)
                            alpha = False
                self.chordProg.append(cur)
            else:
                skip -= 1
            
        self.key = key
        self.timeSig = timeSig

    def Print(self):
        print(*self.chordProg)

