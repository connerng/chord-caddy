import pandas as pd
from chordprog import *
from typing import List

filename = "chord_data.csv"

# fields = ['Name', 'Key', 'BPM', 'Time Signature', 'Chords']

df = pd.read_csv('chord_data.csv')
chords_list: List[ChordProgression] = []

def AddNew(cp: ChordProgression):
    chords_list.append(cp)
    newRow = [cp.name, cp.key, cp.bpm, cp.timeSig, cp.ToString()]
    df.loc[len(df.index)] = [cp.name, cp.key, cp.bpm, cp.timeSig, cp.ToString()]
    df.to_csv('chord_data.csv', index=False)
    print(df)

def Delete(i: int):
    df.drop(index=i, inplace=True)
    print(df)
    df.to_csv('chord_data.csv', index=False)

def Save():
    df.to_csv('chord_data.csv', index=False)

def Reset():
    df = pd.read_csv('chord_data.csv')
    print(df)