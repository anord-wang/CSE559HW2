import argparse
import os
import random

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


def generate_new_motif_list(k, DNA_list, profile):
    new_motif_list = []
    for DNA in DNA_list:
        max_probability = 0
        for i in range(len(DNA) - k):
            new_motif = DNA[i:i + k]
            probability = 1
            for j in range(k):
                probability = probability * profile[Nucleotide_Dictionary[new_motif[j]]][j]
            if probability > max_probability:
                max_probability = probability
                selected_motif = new_motif
        new_motif_list.append(selected_motif)
    return new_motif_list


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


def random_motif_search(k, t, DNA_list, iteration=1500):
    initial_motif_list = random_initialize_motif_list(k, t, DNA_list)
    best_motif_list = initial_motif_list
    best_score = 10000000000
    new_motif_list = initial_motif_list
    for i in range(iteration):
        _, profile = get_profile(k, t, new_motif_list)
        new_motif_list = generate_new_motif_list(k, DNA_list, profile)
        new_score = calculate_score(k, t, new_motif_list)
        if new_score < best_score:
            best_motif_list = new_motif_list
            best_score = new_score
    return best_motif_list, best_score


if __name__ == '__main__':
    # initial
    debug_input_data_folder = './data/hw2q1/RandomizedMotifSearch/inputs/'
    debug_output_data_folder = './data/hw2q1/RandomizedMotifSearch/outputs/'
    test_input_data_folder = './data/hw2q1/rand_testcases/'
    test_output_data_folder = './data/hw2q1/rand_testcases_outputs/'
    # get argument
    parser = argparse.ArgumentParser()
    parser.add_argument('--debug_input_file_folder', type=str, default=debug_input_data_folder)
    parser.add_argument('--debug_output_file_folder', type=str, default=debug_output_data_folder)
    parser.add_argument('--test_input_file_folder', type=str, default=test_input_data_folder)
    parser.add_argument('--test_output_file_folder', type=str, default=test_output_data_folder)
    parser.add_argument('--debug', type=str, default=True)
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
            for i in range(t):
                DNA_list.append(data.split('\n')[1 + i])
            # search motif
            motif_list, score = random_motif_search(k, t, DNA_list)
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
            for i in range(t):
                DNA_list.append(data.split('\n')[1 + i])
            # search motif
            motif_list, score = random_motif_search(k, t, DNA_list)
            print('motif_list: ', motif_list)
            print('score: ', score)
            # save result
            output_file = args.test_output_file_folder + 'output_' + input_file
            with open(output_file, 'a') as of:
                for i in range(t):
                    of.write(str(motif_list[i]) + '\n')
