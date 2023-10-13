from hw2q1 import random_motif_search
from hw2q2 import gibbs_sampling_motif_search
from hw2q1 import generate_consensus as r_generate_consensus
from hw2q2 import generate_consensus as g_generate_consensus

data_path = './data/hw2q3/motif_dataset.txt'
output_file_path = './data/hw2q3/motif_outpot.txt'
with open(data_path, 'r') as f:
    DNA_list = f.readlines()
k = 15
t = len(DNA_list)
r_iteration_list = [1000, 10000, 100000]
g_iteration_list = [1000, 2000, 10000]

with open(output_file_path, 'a') as of:
    for i in range(3):
        print(i)
        of.write('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n')
        print(i)
        of.write('this is the result of the No.' + str(i+1) + ' parameter set: \n')
        of.write('--------------------------------------------------------------\n')
        of.write('now we use random motif search method for ' + str(r_iteration_list[i]) + ' times' + '\n')
        r_motif_list, r_score = random_motif_search(k, t, DNA_list, iteration=r_iteration_list[i])
        r_consensus = r_generate_consensus(k, t, r_motif_list)
        of.write('here is the result of random motif search method: \n')
        of.write('the consensus is: ' + str(r_consensus) + '\n')
        of.write('the score is: ' + str(r_score) + '\n')
        of.write('--------------------------------------------------------------\n')
        of.write('now we use gibbs sampling motif search method for ' + str(g_iteration_list[i]) + ' times' + '\n')
        g_motif_list, g_score = gibbs_sampling_motif_search(k, t, g_iteration_list[i], DNA_list)
        g_consensus = g_generate_consensus(k, t, g_motif_list)
        of.write('here is the result of gibbs sampling motif search method: \n')
        of.write('the consensus is: ' + str(g_consensus) + '\n')
        of.write('the score is: ' + str(g_score) + '\n')
        of.write('\n')

