DEBUGGING = False

class Part():
    def __init__(self, row: int, start_ind: int, value: int):
        self.row = row
        self.start_ind = start_ind
        self.value = value
        self.length = self.get_length()
        self.indexes = range(self.start_ind, self.start_ind + self.length)
    
    def get_length(self) -> int:
        return len(str(self.value))
    
    def is_adjacent_to_symbol(self, index: int, row: int) -> bool:
        if index == self.indexes[-1] + 1:
            return True
        if index == self.start_ind - 1:
            return True
        if index in self.indexes:
            return True
        return False
        
    def __str__(self):
        string = f"Value: {self.value} Row: {self.row} Start index: {self.start_ind}"
        return string
    
    
class Field():
    def __init__(self, field: list[str]):
        self.field = field
        self.parts = self.find_parts()
        
    def find_parts(self) -> list[Part]:
        parts = list()
        for j, row in enumerate(self.field):
            i = 0
            while i < len(row):
                if row[i].isdigit():
                    current_num_list = list()
                    start_i = i
                    while row[i].isdigit() and i < len(row):
                        current_num_list.append(row[i])
                        i += 1
                    parts.append(Part(j, start_i, int("".join(current_num_list))))
                i += 1
        return parts

    def is_engine_part(self, part: Part) -> bool:
        if self.check_left_and_right(part): return True
        if self.check_up_and_down(part): return True
        if self.check_diagonals(part): return True
        return False
        
    def check_left_and_right(self, part: Part) -> bool:
        left_i = part.start_ind - 1
        right_i = part.start_ind + part.length
        if self.check_symbol(left_i, part.row) or\
            self.check_symbol(right_i, part.row):
                return True
        return False
    
    def check_up_and_down(self, part: Part):
        up_row = part.row - 1
        down_row = part.row + 1
        for i in range(part.length):
            if self.check_symbol(part.start_ind + i, up_row):
                return True
            if self.check_symbol(part.start_ind + i, down_row):
                return True
        return False

    def check_diagonals(self, part: Part) -> bool:
        up_row = part.row - 1
        down_row = part.row + 1
        left = part.start_ind - 1
        right = part.start_ind + part.length
        if self.check_symbol(left, up_row): return True
        if self.check_symbol(left, down_row): return True
        if self.check_symbol(right, up_row): return True
        if self.check_symbol(right, down_row): return True
        return False
    
    def check_borders(self, index: int, row: int) -> bool:
        if (index >= 0 and index < len(self.field[0])) and\
            (row >= 0 and row < len(self.field)):
            return True
        return False
    
    def check_symbol(self, index: int, row: int) -> bool:
        if self.check_borders(index, row):
            if self.field[row][index] != "." and self.field[row][index] != "\n":
                return True
        return False
    
    def check_num(self, index: int, row: int) -> bool:
        if self.check_borders(index, row):
            if self.field[row][index].isdigit():
                return True
        return False
    
    def get_engine_parts(self) -> list[Part]:
        return [part for part in self.parts if self.is_engine_part(part)]
    
    def get_not_engine_parts(self) -> list[Part]:
        return [part for part in self.parts if not self.is_engine_part(part)]
    
    def get_engine_numbers(self) -> list[int]:
        return [part.value for part in self.parts if self.is_engine_part(part)]
    
    def get_not_engine_numbers(self) -> list[int]:
        return [part.value for part in self.parts if not self.is_engine_part(part)]
    
    def get_gears_ratios(self):
        gears_ratios = list()
        for i, row in enumerate(self.field):
            for j, value in enumerate(row):
                if value == "*":
                    adjacent_parts = self.find_adjacent_parts(j, i)
                    if len(adjacent_parts) == 2:
                        gears_ratios.append(adjacent_parts[0].value * adjacent_parts[1].value)
        return gears_ratios
        
    def find_adjacent_parts(self, index: int, row: int) -> list[Part]:
        return [part for part in self.get_engine_parts() if part.row in range(row - 1, row + 2) and part.is_adjacent_to_symbol(index, row)]
        
    
class Reader():
    def read_lines(path: str) -> list[str]:
        with open(path, "r") as file:
            return file.readlines()
        
        
class Main():
    def run(self, path: str):
        field = Field(Reader.read_lines(path))
        gear_ratios = field.get_gears_ratios()
        engine_numbers = field.get_engine_numbers()
        engine_parts = field.get_engine_parts()
        if DEBUGGING:
            for part in engine_parts:
                print(part, "engine part:", field.is_engine_part(part), "\n")
        return sum(gear_ratios)
        
app = Main()
print(app.run("day3/task2/values.txt"))