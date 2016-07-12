#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, sys

def rollFile(iterator):
    for item in iterator:
        yield item

def process(rbnFile,sel,kk,vv):

    qso = ''
    rx = ''
    s = ''
    fo = os.path.splitext(os.path.basename(rbnFile))[0] + ".log"
    
    if sel == "1": s = 'CQ'
    if sel == "2": s = 'DE'
    if sel == "3": s = ''

    with open(rbnFile, "r") as r, open(fo, "w") as of:
        print("\nConverting file: " + rbnFile + "...")

        for row in rollFile(r):

            sm = (row[79:81]).strip()

            if s == "CQ" and sm != "CQ":
                continue
            elif s == "DE" and sm == '':
                continue 

            a = row.split()
            date = a[0]
            year, month = date.split('-')[:-1]

            if kk == 0: pass
            elif kk != int(month): continue

            if vv == 0: pass
            elif vv != int(year): continue
                
            try:
                fq = (a[2].split('.')[0]).rjust(5) # freq
                if len(fq) > 5: continue
                stn = ''.join(a[3].split()) # stn spotted, max 13 chars
                stn = (stn[:13]).ljust(14)
                time = ''.join(a[1].split(':',2)[:-1]) # time
                mode = row[74:77]
                if mode == "WPM": mode = "CW"
                rx = a[-1].strip() # skimmer
                rx = (rx[1:-3]).ljust(14)
                qso += "QSO: " + fq + " " + mode + " " + date + " " + time + " " + rx + "599 1      " + stn + "599 1" + "\n"
            except ValueError:
                print("Ignored:" + row, end='')
                continue

        sys.stdout = of    
        print('''START-OF-LOG: 3.0
CREATED-BY: SPOTS2CAB Converter v0.1 by OH6BG
CONTEST: Skimmer Server Analysis
CATEGORY: Skimmer
CLAIMED-SCORE: 0''')
        print("CALLSIGN: " + rx.strip())
        print("OPERATORS: " + rx.strip())
        qso = qso[:-1]
        print(qso)
        print("END-OF-LOG:")
        sys.stdout = sys.__stdout__

sel = 0
kk = -1
vv = -1
filename = "Spots.txt"

print("SPOTS to CABRILLO Converter, v0.1. (c) 2016 OH6BG.\n" + 80 * '.')
while (int(sel) < 1 or int(sel) > 3):
    sel = input("Spots to include? 1) CQ, 2) CQ+DE, or 3) All: ")

while (int(kk) < 0 or int(kk) > 12):
    kk = input("Month? (1-12, 0 = All): ")

while (int(vv) < 0):
    vv = input("Year? (0 = All): ")

sys.__stdout__ = sys.stdout
process(filename,sel,int(kk),int(vv))

print("Completed conversion of file 'Spots.txt' to CABRILLO file 'spots.log'.")

