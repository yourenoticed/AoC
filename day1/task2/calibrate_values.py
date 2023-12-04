DIGITS_LETTERS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

DEBUGGING = True

def calibrate_values(path: str) -> int:
    lines_list = read_lines(path)
    calibration_values = find_calibration_values(lines_list)
    return sum(calibration_values)

def find_calibration_values(values: list[str]) -> list[int]:
    return [get_line(value) for value in values]
            
def get_line(value: str) -> int:
    left = 0
    while left < len(value):
        if not value[left].isdigit():
            left += 1
        else:
            left_num = int(value[left])
            break
            
    right = len(value) -1
    while right >= 0:
        if not value[right].isdigit():
            right -= 1
        else:
            right_num = int(value[right])
            break
        
    if right < 0:
        right = 0
        
    # checking the left and right of digits to find out if there's any
    
    earliest_left_word = check_letter_num(value[:left])
    if earliest_left_word >= 0:
        left_num = earliest_left_word
    
    earliest_right_word = check_letter_num(value[right:], left=False)
    if earliest_right_word >= 0:
        right_num = earliest_right_word
        
    if DEBUGGING:
      print(f'line: {value}left num: {left_num}, right num: {right_num}\n') 
      
    return left_num * 10 + right_num

def check_letter_num(value: str, left=True):
    earliest_val = -1
    if left:
        earliest_ind = len(value)
        for digit in DIGITS_LETTERS.keys():
            if digit in value:
                substr_beginning = value.find(digit)
                if substr_beginning < earliest_ind:
                    earliest_val = DIGITS_LETTERS[digit]
                    earliest_ind = substr_beginning
        return earliest_val
    else:
        earliest_ind = -1
        for digit in DIGITS_LETTERS.keys():
            if digit in value:
                substr_beginning = value.rfind(digit)
                if substr_beginning > earliest_ind:
                    earliest_val = DIGITS_LETTERS[digit]
                    earliest_ind = substr_beginning
        return earliest_val
        
def read_lines(path: str) -> list[str]:
    with open(path, "r") as file:
        return file.readlines()

print(calibrate_values("day1/task2/values.txt"))