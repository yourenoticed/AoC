class Scratchcard():
    def __init__(self, id: int, needed_numbers: list[int], present_numbers: list[int]):
        self.id = id
        self.needed_numbers = needed_numbers
        self.present_numbers = present_numbers
        
    def __str__(self) -> str:
        return f'Card {self.id}: {" ".join(self.needed_numbers)} | {" ".join(self.present_numbers)}'
    
    def find_score(self) -> int:
        matching_amount = self.get_matching_nums_count()
        if matching_amount > 1:
            return 2 ** (matching_amount - 1)
        elif matching_amount == 1:
            return 1
        return 0
    
    def get_matching_nums_count(self):
        matching_amount = 0
        for num in self.present_numbers:
            if num in self.needed_numbers:
                matching_amount += 1
        return matching_amount
    
        
class Scratchcards():
    def __init__(self, info: list[str]):
        self.scratchcards = self.get_scratchcards(info) 
    
    def get_scratchcards(self, lines: list[str]) -> list[Scratchcard]:
        scratchcards = list()
        for line in lines:
            scratchcards.append(self.get_scratchcard(line))
        return scratchcards
    
    def get_scratchcard(self, line: str) -> Scratchcard:
        info_part = line.split(":")
        card_id = int(info_part[0].split()[1].strip())
        needed_numbers, present_numbers = self.get_all_numbers(info_part[1].rstrip("\n").strip())
        
        return Scratchcard(card_id, needed_numbers, present_numbers)

    def get_all_numbers(self, number_line: str) -> tuple(list[int]):
        split_line = number_line.split("|")
        needed_numbers_list = split_line[0].split()
        present_numbers_list = split_line[1].split()
        return (needed_numbers_list, present_numbers_list)
    

class Main():
    def run(self, path: str):
        scratchcards = Scratchcards(Reader.read_lines(path))
        pts = list()
        for scratchcard in scratchcards.scratchcards:
            pts.append(scratchcard.find_score())
        return sum(pts)
        
    
class Reader():
    def read_lines(path: str) -> list[str]:
        with open(path, "r") as file:
            return file.readlines()
        
app = Main()
print(app.run("day4/task1/values.txt"))