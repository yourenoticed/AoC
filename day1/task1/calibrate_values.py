def calibrate_values(path: str) -> int:
    lines_list = read_lines(path)
    calibration_values = find_calibration_values(lines_list)
    return sum(calibration_values)

def find_calibration_values(values: list[str]) -> list[int]:
    return [get_line(value) for value in values]
            
def get_line(value: str):
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
            
    return left_num * 10 + right_num

def read_lines(path: str) -> list[str]:
    with open(path, "r") as file:
        return file.readlines()

print(calibrate_values("day1/task1/values.txt"))