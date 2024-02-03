def find_sum_pairs(numbers_list, target_sum):
    pair_count = 0

    for i in range(len(numbers_list)):
        for j in range(i + 1, len(numbers_list)):
            if numbers_list[i] + numbers_list[j] == target_sum:
                pair_count +=1
                print("pair", pair_count)
                print(numbers_list[i], "--", numbers_list[j])

    print("Number of pairs with sum", target_sum, "is:", pair_count)

# Input values and call the function with the list and target sum 
numbers_list = [2, 7, 4, 1, 3, 6]
target_sum = 10
find_sum_pairs(numbers_list, target_sum)               