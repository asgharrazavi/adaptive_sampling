import os,sys
import numpy as np


names = [
'C1 ',
'C2 ',
'C3 ',
'C4 ',
'C5 ',
'C6 ',
'C7 ',
'C8 ',
'N9 ',
'H10',
'H11',
'H12',
'O13',
'O14',
'H15',
'H16',
'H17',
'H18',
'H19',
'H20',
'H21',
'H22',
'H23',
]

bonds = [
       1,      2,      1,      6,      1,     14,      2,      3,
       2,     13,      3,      4,      3,     17,      4,      5,
       4,      7,      5,      6,      5,     18,      6,     19,
       7,      8,      7,     20,      7,     21,      8,      9,
       8,     22,      8,     23,      9,     10,      9,     11,
       9,     12,     13,     16,     14,     15,
]

angles = [
       1,     14,     15,      1,      6,     19,      1,      2,     13, 
       1,      2,      3,      1,      6,      5,      2,     13,     16,
       2,      3,     17,      2,      3,      4,      2,      1,     14,
       2,      1,      6,      3,      4,      7,      3,      4,      5,
       3,      2,     13,      4,      7,     21,      4,      7,     20,
       4,      7,      8,      4,      5,     18,      4,      5,      6,
       4,      3,     17,      5,      6,     19,      5,      4,      7,
       6,      5,     18,      6,      1,     14,      7,      8,     23,
       7,      8,     22,      7,      8,      9,      8,      9,     12,
       8,      9,     11,      8,      9,     10,      8,      7,     21,
       8,      7,     20,      9,      8,     23,      9,      8,     22,
      10,      9,     12,     10,      9,     11,     11,      9,     12,
      20,      7,     21,     22,      8,     23,
]

dihs = [
       1,      2,      3,      4,      1,      2,      3,     17,
       1,      2,     13,     16,      2,      3,      4,      5,
       2,      3,      4,      7,      2,      1,      6,      5,
       2,      1,      6,     19,      2,      1,     14,     15,
       3,      4,      5,      6,      3,      4,      5,     18,
       3,      4,      7,      8,      3,      4,      7,     20,
       3,      4,      7,     21,      3,      2,     13,     16,
       4,      5,      6,      1,      4,      7,      8,      9,
       4,      7,      8,     22,      4,      7,      8,     23,
       4,      5,      6,     19,      5,      4,      7,      8,
       5,      4,      7,     20,      5,      4,      7,     21,
       6,      1,      2,      3,      6,      1,      2,     13,
       6,      1,     14,     15,      7,      4,      5,      6,
       7,      8,      9,     10,      7,      8,      9,     11,
       7,      8,      9,     12,      7,      4,      5,     18,
      13,      2,      3,      4,     13,      2,      3,     17,
      14,      1,      2,      3,     14,      1,      6,      5,
      14,      1,      2,     13,     14,      1,      6,     19,
      17,      3,      4,      5,     17,      3,      4,      7,
      18,      5,      6,      1,     18,      5,      6,     19,
      20,      7,      8,      9,     20,      7,      8,     22,
      20,      7,      8,     23,     21,      7,      8,      9,
      21,      7,      8,     22,     21,      7,      8,     23,
      22,      8,      9,     10,     22,      8,      9,     11,
      22,      8,      9,     12,     23,      8,      9,     10,
      23,      8,      9,     11,     23,      8,      9,     12,
]

imps = [
       1,       2,       6,      14,       2,       1,       3,      13,
       3,       2,       4,      17,       4,       3,       5,       7,
       5,       4,       6,      18,      19,       1,       5,       6,
]

for i in range(0,len(bonds),2):
        print "% 3s % 3s " %(names[bonds[i]-1], names[bonds[i+1]-1]),

print "\n"
#for i in range(0,len(angles),3):
#        print "%s %s %s " %(names[angles[i]-1], names[angles[i+1]-1], names[angles[i+2]-1]),


#for i in range(0,len(dihs),4):
#        print "%s %s %s %s " %(names[dihs[i]-1], names[dihs[i+1]-1], names[dihs[i+2]-1], names[dihs[i+3]-1]),


for i in range(0,len(imps),4):
        print "%3s %3s %3s %3s " %(names[imps[i]-1], names[imps[i+1]-1], names[imps[i+2]-1], names[imps[i+3]-1]),



