import os,sys
import numpy as np
import json as js

names = np.loadtxt('names',dtype=str)
print names[0:10]

un = np.unique(names)
print "uniq:", un

print "total possible anles:", len(un)*len(un)*len(un)


dih1 = open('/Users/asr2031/Dropbox/pyscripts/Namd/toppar_all/for_anton/from_anton/charmm36_lipids/angle_harm','r')
lines1 = dih1.readlines()

dih2 = open('/Users/asr2031/Dropbox/pyscripts/Namd/toppar_all/for_anton/from_anton/charmm36_lipids_c36chl1/angle_harm','r')
lines2 = dih2.readlines()


dih1 = open('/Users/asr2031/Dropbox/pyscripts/Namd/toppar_all/for_anton/from_anton/charmm36_lipids/angle_harm').read()
l1 = js.loads(dih1)

dih2 = open('/Users/asr2031/Dropbox/pyscripts/Namd/toppar_all/for_anton/from_anton/charmm36_lipids_c36chl1/angle_harm').read()
l2 = js.loads(dih2)

data = []
for u in un:
    for l in range(len(lines1)-2):
	if str(l1[l]['type'][0]) in un and str(l1[l]['type'][1]) in un and str(l1[l]['type'][2]) in un:
            if lines1[l] not in data:
#	        print u
#	   	print l1[l]
# 	        print l, lines1[l+1]
	        data.append(lines1[l+1])

f = open('angle_harm','w')
f.writelines("[\n")
for d in range(len(data)):
    f.writelines(data[d])
    if  ',' not in data[d][-3:] : print d, data[d]
    
f.writelines("]")

f.close()

