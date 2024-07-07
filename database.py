import pandas as pd
import xlrd
import xlwt
import openpyxl
from xlwt import Workbook
from openpyxl import load_workbook
from chordprog import *
import csv

filename = "chord_data.csv"

# fields = ['Name', 'Key', 'BPM', 'Time Signature', 'Chords']

df = pd.read_csv('chord_data.csv')

def AddNew(cp: ChordProgression):
    newRow = [cp.name, cp.key, cp.bpm, cp.timeSig, cp.ToString()]
    df.loc[len(df.index)] = [cp.name, cp.key, cp.bpm, cp.timeSig, cp.ToString()]
    with open(filename, 'a') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(newRow)
    print(df)

def Delete(name: str):
    df.drop(labels=name, axis='index', inplace=True)
    print(df)

print(df)
# Delete("Test(G)")


# cptest = ChordProgression("Test 1", "|C...|Am...|F...|G...|", "4/4", "C", 75)
# AddNew(cptest)
# print(df)