# CSE559HW2
This repository contains my code and files for CSE559 homework 2  
  

**For question 1:**  
The main code is in [hw2q1.py](cse559code/hw2q1.py).  
The output files for 4 samples are in [rand_testcases_outputs](cse559code/data/hw2q1/rand_testcases_outputs).  
There are 5 arguments in this code:  
* '--debug_input_file_folder': This is the folder containing the data you want to use as the input in the debug stage. For example: './data/hw2q1/RandomizedMotifSearch/inputs/'  
* '--debug_output_file_folder': This is the folder containing the data you want to use as the checkpoint in the debug stage. For example: './data/hw2q1/RandomizedMotifSearch/outputs/'  
* '--test_input_file_folder': This is the folder containing the data you want to use as the input in the test stage. For example: './data/hw2q1/rand_testcases/'  
* '--test_output_file_folder': This is the folder where you want to put the result file in the test stage. For example: './data/hw2q1/rand_testcases_outputs/'  
* '--debug': This is a boolean variable, which controls the stage you want to use. If it is True, it means the current stage is the debug stage, otherwise, it is the test stage.  
* The code is under Python 3.11. Please make sure your environment contains 'argparse', 'os', and 'random'.  
  
  
**For question 2:**  
The main code is in [hw2q2.py](cse559code/hw2q2.py).  
The output files for 2 samples are in [gibbs_testcases_outputs](cse559code/data/hw2q2/gibbs_testcases_outputs).  
There are 5 arguments in this code:  
* '--debug_input_file_folder': This is the folder containing the data you want to use as the input in the debug stage. For example: './data/hw2q2/GibbsSampling/inputs/'  
* '--debug_output_file_folder': This is the folder containing the data you want to use as the checkpoint in the debug stage. For example: './data/hw2q2/GibbsSampling/outputs/'  
* '--test_input_file_folder': This is the folder containing the data you want to use as the input in the test stage. For example: './data/hw2q2/gibbs_testcases/'  
* '--test_output_file_folder': This is the folder where you want to put the result file in the test stage. For example: './data/hw2q2/gibbs_testcases_outputs/'  
* '--debug': This is a boolean variable, which controls the stage you want to use. If it is True, it means the current stage is the debug stage, otherwise, it is the test stage.  
The code is under Python 3.11. Please make sure your environment contains 'argparse', 'os', 'random', and 'copy'.  
  
  
**For question 1 and question 2:**  
Sometimes I can get the same result as the given .txt file, but they can’t happen together. And sometimes they have the same score but the motifs are different.  
For example: for Input_1 of question 2  
  - motif_list:  ['CTCGGGGG', 'TGTAAGTG', 'TACAGGCG', 'TTCAGGTG', 'TCCACGTG']  
  - score:  9  
  - result_list:  ['TCTCGGGG', 'CCAAGGTG', 'TACAGGCG', 'TTCAGGTG', 'TCCACGTG']  
  - result_score:  9  
  
  
**For question 3:**  
The main code is in [hw2q3.py](cse559code/hw2q3.py).  
The code is under Python 3.11. Please make sure there are [hw2q1.py](cse559code/hw2q1.py) and [hw2q2.py](cse559code/hw2q2.py).  
The results for different parameters are in file [motif_outpot.txt](cse559code/data/hw2q3/motif_outpot.txt).  
I put my summary as a PDF file on GitHub. The file is [hw1q3_summary_wxy.pdf](hw1q3_summary_wxy.pdf).  
