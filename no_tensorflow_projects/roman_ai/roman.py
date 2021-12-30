def integer_to_roman(number):
    """
    Takes a number and returns a string with the roman
    equivalent.
    """
    roman_dict = {
        1: "I",
        5: "V",
        10: "X",
        50: "L",
        100: "C"
    }

    roman = ""
    stringed = str(number)
    pointer = len(stringed)-1

    if number == 0:
        return 0
    
    # convert each number to the roman equivalent
    while pointer < len(stringed):
        num = int(stringed[pointer])
        mult = 10**(len(stringed)-pointer-1)

        if num <= 3:
            for i in range(num):
                roman += roman_dict[1*mult]

        elif num > 5 and num <= 8:
            roman += roman_dict[5*mult]

            for i in range(num-5):
                roman += roman_dict[1*mult]

        elif num == 4 or num == 9:
            roman += roman_dict[1*mult]

            if num == 4:
                roman += roman_dict[5*mult]

            else:
                roman += roman_dict[10*mult]

        else:
            roman += roman_dict[num*mult]
        
        pointer += 1

    return roman