def computeLPSArray(pat):
    M = len(pat)
    lps = [0] * M

    length = 0  # length of the previous longest prefix suffix

    lps[0] = 0  # lps[0] is always 0
    i = 1

    # the loop calculates lps[i] for i = 1 to M-1
    while i < M:
        if pat[i] == pat[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            # This is tricky. Consider the example.
            # AAACAAAA and i = 7. The idea is similar
            # to search step.
            if length != 0:
                length = lps[length - 1]

                # Also, note that we do not increment i here
            else:
                lps[i] = 0
                i += 1
    return lps

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

pat = "ATCATCT"
lps = computeLPSArray(pat)
z_seq = Z_algorithm(pat)
print('lps: ', lps)
print('z_seq: ', z_seq)
lps__ = [0] * len(pat)
for i in range(len(pat)):
    if z_seq[i] > 0:
        lps__[i + z_seq[i] - 1] = z_seq[i]
print('lps__: ', lps__)