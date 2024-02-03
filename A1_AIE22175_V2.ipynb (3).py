def find_highest_occurence(input_str):
    char_frequency = {}

    for char in input_str:
        # If the character is an alphabet, update its frequency in the dictionary
        if char.isalpha():
            if char in char_frequency:
                char_frequency[char] += 1
            else:
                char_frequency[char] = 1

    # Find the character with the maximum ferquency
    most_common_char = max( char_frequency, key=char_frequency.get)

    # Output the character with its occurency count
    max_occurence_count = char_frequency[most_common_char]            

    print(f"The most common alphabet is '{most_common_char}' with a count of : {max_occurence_count}")

# Input value and call the function, passing the input
given_string = "Bharathteja"
find_highest_occurence(given_string)     