def calculate_eq(input_str):
    """Calculate the equation with only the + and * signs"""
    result = 0
    current_num = 0
    current_mult_block = 1
    is_after_mult = False

    for char in input_str:
        if char == "+":
            if is_after_mult:
                current_mult_block *= current_num
                result += current_mult_block
            else:
                result += current_num
            current_mult_block = 1
            current_num = 0
            is_after_mult = False
        elif char == "*":
            current_mult_block *= current_num
            is_after_mult = True
            current_num = 0
        else:
            current_num = current_num * 10 + int(char)

    if is_after_mult:
        current_mult_block *= current_num
        result += current_mult_block
    else:
        result += current_num

    return result


data = "1+2*3*2+1"
print(calculate_eq(data))
