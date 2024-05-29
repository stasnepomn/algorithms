def sorted_squared_array(array):
    squares = [0 for _ in array]
    smaller_idx = 0
    bigger_idx = len(array) - 1

    for idx in reversed(range(len(array))):
        smaller_val = array[smaller_idx]
        larger_val = array[bigger_idx]

        if abs(smaller_val) > abs(larger_val):
            squares[idx] = smaller_val**2
            smaller_idx += 1
        else:
            squares[idx] = larger_val**2
            bigger_idx -= 1

    return squares
