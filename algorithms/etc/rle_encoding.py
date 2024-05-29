def rle_encoding(input_str):
    if not input_str:
        return ""

    left_idx, right_idx = 0, 0
    result_str = ""

    while right_idx < len(input_str):
        if input_str[left_idx] == input_str[right_idx]:
            right_idx += 1
        else:
            result_str += f"{right_idx - left_idx}{input_str[left_idx]}"
            left_idx = right_idx

    result_str += f"{right_idx - left_idx}{input_str[left_idx]}"

    return result_str


print(rle_encoding("aaaabbbbcccdd"))
print(rle_encoding("a"))
print(rle_encoding("adddbdbdbdbdbddkhdkjdhjhhhhhhsjssssskkkkwwww"))
