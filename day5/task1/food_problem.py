class Food_Problem():
    def __init__(self, values_lines: list[str]):
        self.values_lines = values_lines
        self.map_names = ["seed", "soil", "fertilizer", "water", "light", "temperature", "humidity", "location"]
    
    def get_seeds(self) -> list[int]:
        seed_nums_str = self.values_lines[0].split(":")[1]
        return [int(seed_num) for seed_num in seed_nums_str.split()]
    
    # map_name must be in format 'smth-to-smth'
    def get(self, map_name: str) -> list[tuple[int]]:
        i = 0
        num_list = list()
        while i < len(self.values_lines):
            if map_name in self.values_lines[i]:
                i += 1
                while i < len(self.values_lines) and self.values_lines[i] != "\n":
                    num_list.append(self.parse_nums(self.values_lines[i]))
                    i += 1
                break
            i += 1 
        return num_list
    
    def parse_nums(self, line: str) -> tuple[int]:
        nums_list = line.split()
        return tuple([int(num) for num in nums_list])
    
    def get_matching(self, what: str, what_num: int, to_what: str) -> int:
        for num_line in self.get(what + "-to-" + to_what):
            if what_num in range(num_line[1], num_line[1] + num_line[2]):
                return (what_num - num_line[1]) + num_line[0]
        return what_num
    
    def get_locations(self) -> int:
        seeds = self.get_seeds()
        nums = list()
        for seed in seeds:
            num = seed
            for i in range(len(self.map_names) - 1):
                num = self.get_matching(self.map_names[i], num, self.map_names[i + 1])
            nums.append(num)
        return nums
        
        
class Reader():
    def read_lines(self, path: str) -> list[str]:
        with open(path, "r") as file:
            return file.readlines()
        
        
class Main():
    def run(self, path: str):
        file = Reader()
        solver = Food_Problem(file.read_lines(path))
        return min(solver.get_locations())


app = Main()
print(app.run("day5/task1/values.txt"))