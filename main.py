from transposer import *
from tkinter import *
from chordprog import *

test_cp_str = "|C...|Am...|G...|F...|"
test_str_2 = "|Am...|C...|Em...|D...|"
cp = ChordProgression(test_cp_str, "4/4", "C")
print(cp.timeSig)
print(cp.key)
print(cp)

cp2 = ChordProgression(test_str_2, "4/4", "G")
print(cp2.timeSig)
print(cp2.key)
print(cp2)

cp3 = TransposeCP(cp, 1)
print(cp3.timeSig)
print(cp3.key)
print(cp3)