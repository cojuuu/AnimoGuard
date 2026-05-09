import random
import string

def break_continuity(base_string):
    new_base_string = base_string[0]
    prev_char = base_string[0]
    repeat_count = 1
    
    for cur_char in base_string[1:]:
        if cur_char == prev_char:
            repeat_count += 1
            
            if repeat_count == 3:
                if prev_char != 'X':
                    prev_char = 'X'
                    new_base_string += 'X'
                elif prev_char != 'x':
                    prev_char = 'x'
                    new_base_string += 'x'
                repeat_count = 1
            else:
                new_base_string += cur_char
        else:
            prev_char = cur_char
            new_base_string += cur_char
            repeat_count = 1
    
    return new_base_string
        

def break_patterns(base_string, id_num):
    restricted_patterns = ["qwerty", "asdf", "1234"]
    
    for i in range(0, 4):
        restricted_patterns.append(id_num[i:i+5])
    
    for pattern in restricted_patterns:
        base_string = base_string.replace(pattern, f"{pattern[0:2]}X{pattern[3:]}")
        
    return base_string


def substitute_letters(base_string):
    sub_numerals = {
    'B': ['8'],
    'C': ['6'],
    'G': ['9', '6'],
    'L': ['1'],
    'O': ['0'],
    'T': ['7'],
    'Z': ['2']
    }

    sub_specials = {
        'A': ['@', '&'],
        'E': ['#'],
        'H': ['#'],
        'I': ['!'],
        'L': ['!'],
        'P': ['%'],
        'S': ['$']
    }
    
    special_count = 0
    numeral_count = 0
    new_base_string = base_string[0]
    for char in base_string[1:]:
        if char.capitalize() in sub_numerals and numeral_count != 1:
            new_base_string += random.choice(sub_numerals[char.capitalize()])
            numeral_count += 1
        elif char.capitalize() in sub_specials and special_count != 2:
            new_base_string += random.choice(sub_specials[char.capitalize()])
            special_count += 1
        else:
            new_base_string += char
    
    return new_base_string
    

def break_palindrome(base_string):
    if base_string == base_string[::-1]:
        base_string += "!"
    return base_string


def final_check(base_string):
    special_count = 0
    upper_count = 0
    lower_count = 0
    numeral_count = 0
    
    for char in base_string:
        if not char.isalnum():
            special_count += 1
        elif char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
        elif char.isdigit():
            numeral_count += 1 

    while True:
        if special_count < 2:
            base_string += random.choice(string.punctuation)
            special_count += 1
        elif upper_count < 1:
            base_string += random.choice(string.ascii_letters).upper()
            upper_count += 1
        elif lower_count < 1:
            base_string += random.choice(string.ascii_letters).lower()
            lower_count += 1
        elif numeral_count < 1:
            base_string += str(random.randint(0, 9))
            numeral_count += 1 
        else:
            break

    return base_string
        


def generate_password(base_string, id_num):
    return final_check(break_palindrome(substitute_letters(break_patterns(break_continuity(base_string) , id_num))))
    

def main():
    while True:
        try:
            id_num = input("Input ID number: ")
        except ValueError:
            print("Invalid input!")
        else:
            if len(id_num) != 8 or not(75 <= int(id_num[0:3]) <= 126):
                print("Invalid ID number!")
            else:
                break
    
    while True:
        base_string = input("Input base base_string: ")
        if not base_string[0].isalpha():
            print("First letter must be an alphabetic character!")
        elif len(base_string) < 15:
            print("Minimum length should be at least 15!")
        else:
            break
        
    print(f"Generated password: {generate_password(base_string, id_num)}")
    
main()