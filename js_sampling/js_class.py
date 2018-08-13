########
# python class for performing molecular dynamics 
########
def get_msm_pops(tprob):
    evals, ev = msm_analysis.get_eigenvectors(tprob, 2)
    print "first eigen value from msmbuilder:\t", np.max(evals)
    return ev[:,np.argmax(evals)]

class jsd:

    """
    inputs:
    1.(wt)counts.txt        (obtained by using tCounts.mtx and change_counts_mtx2.py script)  
    2.(tz)counts.txt
    3.(wt)Populations.dat   (obtained by using Populations.dat and change_populations.py script)
    4.(tz)Populations.dat
    5.(wt+tz)Populations.dat
    output:
    JSD for each state and contour plots
    """

    def __init__(self, counts1, counts2):

	"""counts are in the form of (num_states ** 2, num_states ** 2, num_states **2)
	first element: state that transition starting from (i)
	second element: state transition going to (j)
	third element: number of counts from i to j
	"""
	self.num_states = int(np.sqrt(counts1.shape[0])) 
	print "num_states:\t", self.num_states
	print "counts.shape:\t", counts1.shape, counts2.shape
		
    def get_tProb(self, counts):
	counts = counts[:,2]
	tprob = copy.deepcopy(counts)
	for i in range(self.num_states):
	    c = counts[ i * self.num_states : i * self.num_states + self.num_states ]
	    if np.sum(c) != 0 :
	        tprob[ i * self.num_states : i * self.num_states + self.num_states ] = c / float(np.sum(c))
#	    else :
#	        print " there is no count into or out of state:\t", i
	    #there should be test that confirms tCounts.mtx is symmentric  
    	return tprob
    
#    self.tProb1 = self.get_tProb(counts1)
#    self.tProb2 = self.get_tProb(counts2)
#    self.comb_tProb = self.get_tProb(counts1 + counts2)

    def get_populations(self,tProb):
	t_prob = np.reshape(tProb, (self.num_states,self.num_states))
	print "tProb.shape:\t", t_prob.shape
	#now we have a square transition probability matrix

	def _check_tProb(tprobs,num_states):
	    for i in range(num_states):
		norm = np.sum(tprobs[ i * num_states : i * num_states + num_states ])
		if norm != 0 and (norm > 1.1 or norm < 0.9) :
		    print "state:\t", i, "\tis not row normalized, sum(rows):\t", norm


   	_check_tProb(tProb,self.num_states)
	
	eigen_values, eigen_vectors = np.linalg.eigh(t_prob)
	first_eigenvalue = np.max(eigen_values)
	if first_eigenvalue != 1.0 :
	    print "eigen value calculation failed, max(eigen_value):\t", first_eigenvalue
	    print "using msmbuilder functions to get populations..."
	    populations = get_msm_pops(t_prob) 
	else:
	    populations = eigen_vectors[:,np.argmax(eigen_values)]
	
	return populations

#    self.populations1 = self.get_populations(self.tProb1)
#    self.populations2 = self.get_populations(self.tProb2)
#    self.comb_populations = self.get_populations(self.comb_tProb)

    def H_for_one_state(self, tprobs, populations, state, num_states):
	tProbs = tprobs[ state * num_states : state * num_states + num_states ]
  	t_ln_t = 0.0 
	for i in range(num_states):
	    if tProbs[i] != 0:
		t_ln_t += tProbs[i] * np.log(tProbs[i])
	h = -1.0 *  populations[state] * t_ln_t
	return h

    def jsd_for_each_state(self, tP1, tP2, p1, p2, comb_tP, comb_p, state, num_states):
	h1 = self.H_for_one_state(tP1, p1, state, num_states)
	h2 = self.H_for_one_state(tP2, p2, state, num_states)
	h_comb = self.H_for_one_state(comb_tP, comb_p, state, num_states)
	return h_comb - 0.5 * h1 - 0.5 * h2

    def jsd_for_all_states(self):
	jsd = []
	tProb1 = self.get_tProb(counts1)
	tProb2 = self.get_tProb(counts2)
	comb_tProb = self.get_tProb(counts1 + counts2)
	populations1 = self.get_populations(tProb1)
	populations2 = self.get_populations(tProb2)
	comb_populations = self.get_populations(comb_tProb)

	for i in range(self.num_states):
	    jsd.append(self.jsd_for_each_state(tProb1, tProb2, populations1, populations2, 
		       comb_tProb, comb_populations, i, self.num_states))
	return jsd




if __name__ == "__main__" :
    
    import os,sys

    usage = """\ninputs:
1.counts1.txt     (use chane_counts_mtx2.py script to get this)
2.counts2.txt
outpu:
jsd for each state
"""

    if len(sys.argv) < 3 :
	print usage
	sys.exit(1)

    import numpy as np
    import copy
    from msmbuilder import msm_analysis

    counts1 = np.loadtxt(sys.argv[1])
    counts2 = np.loadtxt(sys.argv[2])
    JSD = jsd(counts1, counts2)
    jsds = JSD.jsd_for_all_states()
    
    np.savetxt('jsd.txt', jsds)

    print "%s" %('-' * 30) , "\nstate\t\tJSD\n", "%s" %('-' * 30)
    for i in range(len(jsds)):
	print i, "\t", jsds[i]

