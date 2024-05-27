def validate_subsequence(array, sequence):
    seq_idx = 0
    for item in array:
        if item == sequence[seq_idx]:
            seq_idx += 1
        if seq_idx == len(sequence):
            return True
    return False
