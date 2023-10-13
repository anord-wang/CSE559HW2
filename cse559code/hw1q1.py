import argparse
import os


def Z_algorithm(seq):
    n = len(seq)
    Z_seq = [0 for _ in range(n)]
    left_sign = -1
    right_sign = -1
    for i in range(1, n):
        if i > right_sign:
            left_sign = i
            right_sign = i
            while right_sign < n and seq[right_sign - left_sign] == seq[right_sign]:
                right_sign = right_sign + 1
            Z_seq[i] = right_sign - left_sign
            right_sign = right_sign - 1
        else:
            k = i - left_sign
            if Z_seq[k] < right_sign - i + 1:
                Z_seq[i] = Z_seq[k]
            else:
                left_sign = i
                while right_sign < n and seq[right_sign - left_sign] == seq[right_sign]:
                    right_sign = right_sign + 1
                Z_seq[i] = right_sign - left_sign
                right_sign = right_sign - 1
    return Z_seq


def Z_based_pattern_match(original_DNA_seq, pattern_seq):
    con_seq = pattern_seq + original_DNA_seq
    Z_seq = Z_algorithm(con_seq)
    print('Z_seq: ', Z_seq)
    match_position_list = []
    for i in range(len(pattern_seq), len(Z_seq)):
        if Z_seq[i] >= len(pattern_seq):
            match_position_list.append(i - len(pattern_seq) + 1)
    return match_position_list


if __name__ == '__main__':
    # set parameters
    input_data_folder = './data/hw1q1/samples/'
    output_data_folder = './data/hw1q1/output/'
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_file_folder', type=str, default=input_data_folder)
    parser.add_argument('--output_file_folder', type=str, default=output_data_folder)
    args = parser.parse_args()

    # read file and calculate
    input_files = os.listdir(args.input_file_folder)
    for input_file in input_files:
        index = input_file.replace('sample_', '')
        with open(args.input_file_folder + input_file, 'r') as f:
            data = f.read()
        t = data.split()[0]
        p = data.split()[1]
        match_position = Z_based_pattern_match(t, p)
        # output_file = args.output_file_folder + 'sol_' + str(index)
        # with open(output_file, 'a') as of:
        #     for i in range(len(match_position)):
        #         of.write(str(match_position[i]) + '\n')
