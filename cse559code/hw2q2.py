import argparse
import os
import random
import copy

Nucleotide_Dictionary = {'A': 0, 'G': 1, 'C': 2, 'T': 3}


def random_initialize_motif_list(k, t, DNA_list):
    initial_motif_list = []
    for i in range(t):
        start_position = random.randint(0, len(DNA_list[i]) - k)
        initial_motif_list.append(DNA_list[i][start_position:start_position + k])
    return initial_motif_list


def get_profile(k, t, motif_list):
    profile = [[1] * k for _ in range(4)]
    for motif in motif_list:
        for i in range(k):
            if motif[i] == 'A':
                profile[0][i] = profile[0][i] + 1
            elif motif[i] == 'G':
                profile[1][i] = profile[1][i] + 1
            elif motif[i] == 'C':
                profile[2][i] = profile[2][i] + 1
            elif motif[i] == 'T':
                profile[3][i] = profile[3][i] + 1
    profile_after = [[item / (t + 4) for item in profile[index]] for index in range(4)]
    return profile, profile_after


def generate_new_motif(k, DNA, profile):
    motif_probability_list = []
    for i in range(0, len(DNA) - k):
        current_motif = DNA[i:i + k]
        probability = 1
        for j in range(0, k):
            probability = probability * profile[Nucleotide_Dictionary[current_motif[j]]][j]
        motif_probability_list.append(probability)
    indices = list(range(0, len(DNA) - k))
    start_position = random.choices(indices, motif_probability_list)[0]
    selected_motif = DNA[start_position:start_position + k]
    return selected_motif


def calculate_score(k, t, motif_list):
    score = 0
    consensus = generate_consensus(k, t, motif_list)
    for i in range(t):
        for j in range(k):
            if motif_list[i][j] != consensus[j]:
                score = score + 1
    return score


def generate_consensus(k, t, motif_list):
    profile, _ = get_profile(k, t, motif_list)
    consensus = ''

    for j in range(k):
        threshold = 0
        frequent_symbol = ''
        for i in range(4):
            if profile[i][j] > threshold:
                threshold = profile[i][j]
                frequent_symbol = list(Nucleotide_Dictionary.keys())[list(Nucleotide_Dictionary.values()).index(i)]
        consensus = consensus + frequent_symbol

    return consensus


def gibbs_sampling_motif_search(k, t, r, DNA_list, random_intial=30):
    best_motif_list_out = []
    best_score_out = 10000000000
    for index in range(random_intial):
        initial_motif_list = random_initialize_motif_list(k, t, DNA_list)
        best_motif_list_in = initial_motif_list
        best_score_in = 10000000000
        new_motif_list = initial_motif_list
        for i in range(r):
            index = random.randint(0, t - 1)
            rest_motif_list = copy.deepcopy(new_motif_list)
            del rest_motif_list[index]
            _, profile = get_profile(k, t, rest_motif_list)
            new_motif_list[index] = generate_new_motif(k, DNA_list[index], profile)
            new_score = calculate_score(k, t, new_motif_list)
            if new_score < best_score_in:
                best_score_in = new_score
                best_motif_list_in = new_motif_list
        if best_score_in < best_score_out:
            best_score_out = best_score_in
            best_motif_list_out = best_motif_list_in
    return best_motif_list_out, best_score_out


if __name__ == '__main__':
    # initial
    debug_input_data_folder = './data/hw2q2/GibbsSampling/inputs/'
    debug_output_data_folder = './data/hw2q2/GibbsSampling/outputs/'
    test_input_data_folder = './data/hw2q2/gibbs_testcases/'
    test_output_data_folder = './data/hw2q2/gibbs_testcases_outputs/'
    # get argument
    parser = argparse.ArgumentParser()
    parser.add_argument('--debug_input_file_folder', type=str, default=debug_input_data_folder)
    parser.add_argument('--debug_output_file_folder', type=str, default=debug_output_data_folder)
    parser.add_argument('--test_input_file_folder', type=str, default=test_input_data_folder)
    parser.add_argument('--test_output_file_folder', type=str, default=test_output_data_folder)
    parser.add_argument('--debug', type=str, default=False)
    args = parser.parse_args()
    # for debug
    if args.debug:
        # get file
        input_files = os.listdir(args.debug_input_file_folder)
        for input_file in input_files:
            # read file
            index = input_file.replace('input_', '')
            with open(args.debug_input_file_folder + input_file, 'r') as f:
                data = f.read()
            # get data
            DNA_list = []
            k = int(data.split('\n')[0].split()[0])
            t = int(data.split('\n')[0].split()[1])
            r = int(data.split('\n')[0].split()[2])
            for i in range(t):
                DNA_list.append(data.split('\n')[1 + i])
            # search motif
            motif_list, score = gibbs_sampling_motif_search(k, t, r, DNA_list)
            print('motif_list: ', motif_list)
            print('score: ', score)
            # check result
            output_file = args.debug_output_file_folder + 'output_' + str(index)
            with open(output_file, 'r') as of:
                data_out = of.read()
                result_list = []
                for i in range(t):
                    result_list.append(data_out.split('\n')[i])
                result_score = calculate_score(k, t, result_list)
                print('result_list: ', result_list)
                print('result_score: ', result_score)
                for i in range(t):
                    if motif_list[i] != data_out.split('\n')[i]:
                        print('not match!!!!!!!!!!!!!!!!!')
                print('All Done')
    # for test
    else:
        # get file
        input_files = os.listdir(args.test_input_file_folder)
        for input_file in input_files:
            # read file
            with open(args.test_input_file_folder + input_file, 'r') as f:
                data = f.read()
            # get data
            DNA_list = []
            k = int(data.split('\n')[0].split()[0])
            t = int(data.split('\n')[0].split()[1])
            r = int(data.split('\n')[0].split()[2])
            for i in range(t):
                DNA_list.append(data.split('\n')[1 + i])
            # search motif
            motif_list, score = gibbs_sampling_motif_search(k, t, r, DNA_list)
            print('motif_list: ', motif_list)
            print('score: ', score)
            # save result
            output_file = args.test_output_file_folder + 'output_' + input_file
            with open(output_file, 'a') as of:
                for i in range(t):
                    of.write(str(motif_list[i]) + '\n')
