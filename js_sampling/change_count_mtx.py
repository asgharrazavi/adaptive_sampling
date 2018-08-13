import os,sys

usage = """inputs:
1.(wt)Mapping.dat
2.(wt)count matrix without first three lines (so that numpy.loadtxt can open it)
output:
(mod_count_mtx.txt) modified count matrix with length (len(mapping.dat))**2
"""
if len(sys.argv) < 3 :
    print usage
    sys.exit(1) 

import numpy as np
import copy

mapping = np.loadtxt(sys.argv[1])
try : 
    counts = np.loadtxt(sys.argv[2])
except :
    os.system('sed 1,3d %s > temp_counts.txt' %sys.argv[2])
    counts = np.loadtxt('temp_counts.txt')
    os.system('rm temp_counts.txt')

num_maped_states = int(np.max(mapping))
num_states = len(mapping)

print "numer of states after trimming:\t", num_maped_states + 1
print "total number of states:\t", num_states

def change_count_mtx_indx(num_mapped_states,counts):
    counts_indx_changed = copy.deepcopy(counts)
    for i in range(1,num_mapped_states + 2):
	oo = np.where(mapping == i - 1)[0]
	h = np.where(counts == i)
	hh = (h[1] != 2)
	counts_indx_changed[h[0][hh],h[1][hh]] = oo + 1
    return counts_indx_changed

def add_zeros(counts_indx_changed):
    trimed_states = np.where(mapping == -1 )[0]
    print "trimmed states: ", trimed_states
    final_count_mtx = np.ones((num_states,num_states,1)) * -1
    ii = 0
    for i in range(num_states):
	for j in range(num_states-1):
	    if i not in trimed_states : 
		if counts_indx_changed[ii][0] == i + 1 and counts_indx_changed[ii][1] == j + 1 : 
		    final_count_mtx[i][j] = counts_indx_changed[ii][2]
		    ii += 1
		else : 
		    final_count_mtx[i][j] = 0
	    else:
		final_count_mtx[i][j] = 0
    return final_count_mtx

def write_counts_to_txt(final_count_mtx):
    f = open('mod_count_mtx.txt','w')
    for i in range(num_states):
	for j in range(num_states):
	    f.write('%s\t%s\t%s\n' %(i+1, j+1, final_count_mtx[i][j][0]))
    f.close()

step1 = change_count_mtx_indx(num_maped_states,counts)
step2 = add_zeros(step1)
step3 = write_counts_to_txt(step2)

os.system("sed 's/-1/0/g' mod_count_mtx.txt > mod_count_mtx2.txt ")
os.system('mv mod_count_mtx2.txt mod_count_mtx.txt ')




    

