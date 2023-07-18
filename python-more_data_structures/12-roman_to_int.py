#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_values = {
        'I': 1, 'V': 5, 'X': 10,
        'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }
    result = 0
    roman_index = roman_values[roman_string[i]]

    for i in range(len(roman_string)):
        if i > 0 and roman_index > roman_values[roman_string[i - 1]]:
            result += roman_index - 2 * roman_values[roman_string[i - 1]]
        else:
            result += roman_index
    return result
