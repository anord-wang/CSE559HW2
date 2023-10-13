# Python program for KMP Algorithm
def KMPSearch(pat, txt):
    M = len(pat)
    N = len(txt)

    # create lps[] that will hold the longest prefix suffix
    # values for pattern
    lps = [0] * M
    j = 0  # index for pat[]
    j_list = []
    # Preprocess the pattern (calculate lps[] array)
    lps = computeLPSArray(pat, M, lps)

    i = 0  # index for txt[]
    while i < N:
        # print('index:', i)
        # print('pat index:', j)
        j_list.append(j)
        if pat[j] == txt[i]:
            i += 1
            j += 1

        if j == M:
            print("Found pattern at index", str(i - j))
            j = lps[j - 1]

        # mismatch after j matches
        elif i < N and pat[j] != txt[i]:
            # Do not match lps[0..lps[j-1]] characters,
            # they will match anyway
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    print(j_list)


def KMPSearch_gai(pat, lps, txt):
    M = len(pat)
    N = len(txt)

    # create lps[] that will hold the longest prefix suffix
    # values for pattern
    j = 0  # index for pat[]
    j_list = []

    # Preprocess the pattern (calculate lps[] array)

    i = 0  # index for txt[]
    while i < N:
        # print('index:', i)
        # print('pat index:', j)
        j_list.append(j)
        if pat[j] == txt[i]:
            i += 1
            j += 1

        if j == M:
            print("Found pattern at index", str(i - j))
            j = lps[j - 1]

        # mismatch after j matches
        elif i < N and pat[j] != txt[i]:
            # Do not match lps[0..lps[j-1]] characters,
            # they will match anyway
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    print(j_list)


def computeLPSArray(pat, M, lps):
    len = 0  # length of the previous longest prefix suffix

    lps[0] = 0  # lps[0] is always 0
    i = 1

    # the loop calculates lps[i] for i = 1 to M-1
    while i < M:
        if pat[i] == pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            # This is tricky. Consider the example.
            # AAACAAAA and i = 7. The idea is similar
            # to search step.
            if len != 0:
                len = lps[len - 1]

                # Also, note that we do not increment i here
            else:
                lps[i] = 0
                i += 1
    return lps


# txt = "TCATCATGATGATCATCT"
txt = "TCATCACATCATCT"
pat = "ATCATCT"
M = len(pat)
lps = [0] * M
print(lps)
lps = computeLPSArray(pat, M, lps)
print(lps)
print('original search')
KMPSearch(pat, txt)
print('improved search')
lps_ = [0, 0, 0, 0, 3, 0, 0]
KMPSearch_gai(pat, lps_, txt)
