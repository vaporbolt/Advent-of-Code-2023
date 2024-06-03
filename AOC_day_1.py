import sys
import functools

digits_text = {}
digits_text["zero"] = "0"
digits_text["one"] = "1"
digits_text["two"] = "2"
digits_text["three"] = "3"
digits_text["four"] = "4"
digits_text["five"] = "5"
digits_text["six"] = "6"
digits_text["seven"] = "7"
digits_text["eight"] = "8"
digits_text["nine"] = "9"



def main():
    input_file = sys.argv[1]
    input_text = open(input_file, "r").read()
    input_list = input_text.split("\n")
    input_values = map(parse_number, input_list)
    calibration_value = sum(input_values)
    print(calibration_value)

"Gets the number determined by first and last digit of the text"
def parse_number(text):
    word_digits = get_word_digits(text)
    number_digits = get_number_digits(text)
    # combine both digits into one list
    list_of_digits = []
    list_of_digits.extend(number_digits)
    list_of_digits.extend(word_digits)
    # sort smallest to largest
    list_of_digits.sort(key=lambda x: x[0])
    #print(list_of_digits)
    #grab the first occurance and the last occurance (third number occurance if last is None)
    digits = [None, None]
    digits[0] = list_of_digits[0][1]
    # itterate backwards to find non Non Number
    for tuple in reversed(list_of_digits):
        if tuple[1] is not None:
            digits[1] = tuple[1]
            break


    #print(digits[0])
    text_num = ""
    for digit in digits:
        if digit is not None:
            text_num+= (digit)
    if len(text_num) == 1:
        text_num += text_num  
   # print(text_num)     
    num = int(text_num)
    return num


# return list of size 2 of tuples of the word numbers[1] and their positions[0].
def get_word_digits(text):
    digits = []
    for digit in list(digits_text.keys()):
        index = text.find(digit)
        r_index = text.rfind(digit)
        if index != -1:
            #print(digit)
            digits.append((index, digits_text[digit]))
            digits.append((r_index, digits_text[digit]))
    return digits            

# return list of size 2 of tuples of the word numbers[1] and their positions[0].
def get_number_digits(text):
    digits = []
    digit_text_so_far = ""
    for index, char in enumerate(text):
        digit_text_so_far += char
        if char.isdigit():
            digits.append((index, char))
    return digits            

main()