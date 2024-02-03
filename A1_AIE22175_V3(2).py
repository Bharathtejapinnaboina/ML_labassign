def find_min_and_max(input_list):
    if not input_list:
        print("Empty list. Range determination not possible.")
        return None 
    
    Min_value = max_value = input_list[0]

    for num in input_list[1:]:
        if num < min_value:
            min_value = num
        if num > max_value:
            max_value = num

    return min_value, max_value

def calculate_ange(min_value, max_value):
    return max_value - min_value

def determine_and_print_range(input_list):
    if len(input_list) < 2:
        print("Insufficient elements for range determination.")
        return None
    
    print("Range determination is possible.")
    min_val, max_val = find_min_and_max(input_list)
    range_val = calculate_range(min_val, max_val)

    print("Minimum value:", min_val)
    print("Maximum value:", max_val)
    print("Range:", range_val)
    return range_val

my_list - [5, 3]
result = determine_and_print_range(my_list)
