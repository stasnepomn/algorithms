def two_number_sum(array, target):
    seen_nums = set()
    for num in array:
        needed_num = target - num
        if needed_num in seen_nums:
            return [num, needed_num]
        else:
            seen_nums.add(num)
    return []
