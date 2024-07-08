import pandas as pd
from chordprog import *

filename = "chord_data.csv"

# fields = ['Name', 'Key', 'BPM', 'Time Signature', 'Chords']

df = pd.read_csv('chord_data.csv')

def AddNew(cp: ChordProgression):
    newRow = [cp.name, cp.key, cp.bpm, cp.timeSig, cp.ToString()]
    df.loc[len(df.index)] = [cp.name, cp.key, cp.bpm, cp.timeSig, cp.ToString()]
    df.to_csv('chord_data.csv', index=False)
    print(df)

def Delete(i: int):
    df.drop(index=i, inplace=True)
    print(df)
    df.to_csv('chord_data.csv', index=False)

print(df)
# Delete("Test(G)")


# cptest = ChordProgression("Test 1", "|C...|Am...|F...|G...|", "4/4", "C", 75)
# AddNew(cptest)
# print(df)