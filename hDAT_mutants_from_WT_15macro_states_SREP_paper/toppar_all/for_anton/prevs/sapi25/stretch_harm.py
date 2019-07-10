import os,sys
import numpy as np

names = np.loadtxt('names',dtype=str)
print names[0:10]

un = np.unique(names)
print "uniq:", un

dih1 = open('/Users/asgharrazavi/Dropbox/pyscripts/Namd/toppar_all/stream/lipid/for_anton/from_anton/charmm36_lipids/stretch_harm','r')
lines1 = dih1.readlines()

dih2 = open('/Users/asgharrazavi/Dropbox/pyscripts/Namd/toppar_all/stream/lipid/for_anton/from_anton/charmm36_lipids_c36chl1/stretch_harm','r')
lines2 = dih2.readlines()

print "lens:", len(lines1), len(lines2)

lines = lines1 + lines2

print "len(lines):", len(lines)


data = []
for u in un:
    for l in lines:
        if u in l and l not in data:
	    data.append(l)

f = open('stretch_harm','w')
f.writelines("[\n")
for d in range(len(data)):
    f.writelines(data[d])
    if  ',' not in data[d][-3:] : print d, data[d]
    
f.writelines("]")

f.close()

