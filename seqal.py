def seqal(seq1, seq2, match=1, mismatch=-1, gap=-2):
    n, m = len(seq1), len(seq2)
    grid = [[0]*(m+1) for _ in range(n+1)]
    # outermost row/column compare sequence with gap, hence gap length = length of sequence being considered
    for i in range(n+1): grid[i][0] = i * gap
    for j in range(m+1): grid[0][j] = j * gap

    for i in range(1, n+1):
        for j in range (1, m+1):
            score = match if seq1[i-1] == seq2[j-1] else mismatch
            grid[i][j] = max(grid[i-1][j-1] + score, grid[i-1][j] + gap, grid[i][j-1] + gap)

    # traceback
    align1, align2 = "", ""
    i, j = n, m # new vars can be decremented without altering grid dimensions
    while i > 0 and j > 0:
        score = match if seq1[i-1] == seq2[j-1] else mismatch
        if grid[i][j] == grid[i-1][j-1] + score:
            align1, align2 = seq1[i-1] + align1, seq2[j-1] + align2
            i, j = i-1, j-1
        elif grid[i][j] == grid[i-1][j] + gap:
            # if moved vertically, haven't progressed through seq2, hence add a gap there
            align1, align2 = seq1[i-1] + align1, "-" + align2
            i -= 1
        else:
            align1, align2 = "-" + align1, seq2[j-1] + align2
            j -= 1
    # account for sequence length mismatches by adding gaps w/ associated penalties, and prepending remaining sequence
    while i > 0:
        align1, align2 = seq1[i-1] + align1, "-" + align2
        i -= 1
    while j > 0:
        align1, align2 = "-" + align1, seq2[j-1] + align2
        j -= 1
    return f"{align1}\n{align2}\nscore: {grid[n][m]}\n"

print("\ntests:\n")
print(seqal("ACGT", "ACT"))
print(seqal("GATTACAGATTACA","GATCACAGATCACACCGA"))
print(seqal("GATCATAGACTGATGAAATC","CGATCAGCTTAGACGTACGAAGCTA"))
