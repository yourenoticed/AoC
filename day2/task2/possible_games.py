CONFIGURATION = {
    "red": 12,
    "green": 13,
    "blue": 14
}
DEBUGGING = False

class Game():
    def __init__(self, id: int, attempts: list[dict[str: int]]):
        self.id = id
        self.attempts = attempts

    def is_game_possible(self, configuration: str) -> bool:
        for attempt in self.attempts:
            if self.check_color_intersection(attempt, configuration):
                if not self.check_color_presence(attempt, configuration):
                    return False
            else:
                return False
        return True

    def check_color_intersection(self, attempt: dict[str: int], configuration: dict[str: int]) -> bool:
        for color in attempt:
            if color not in configuration:
                return False
        return True
    
    # color amount in any attempt has to be less than or equal to the one in configuration
    def check_color_presence(self, attempt: dict[str: int], configuration: dict[str: int]):
        for color in attempt:
            if configuration.get(color) < attempt.get(color):
                return False
        return True
    
    def get_needed_amount_of_colors(self) -> list[int]:
        needed_colors = dict()
        for attempt in self.attempts:
            for color in attempt:
                if color in needed_colors and needed_colors[color] < attempt[color]:
                    needed_colors[color] = attempt[color]
                elif color not in needed_colors:
                    needed_colors[color] = attempt[color]
        return list(needed_colors.values())
        
    
class Main():
    # returns sum of products of needed colors
    def run(self, path: str) -> int:
        lines = self.read_lines(path)
        games = self.get_games(lines)
        powers = [self.get_multiplication(game.get_needed_amount_of_colors()) for game in games]
        
        return sum(powers)
    
    def get_multiplication(self, nums: list[int]):
        product = 1
        for num in nums:
            product *= num
        return product            
    
    def read_lines(self, path: str) -> list[str]:
        with open(path, "r") as file:
            return file.readlines()
    
    def get_games(self, lines: list[str]) -> list[Game]:
        return [self.get_game(line) for line in lines]
    
    # Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    def get_game(self, line: str) -> Game:
        info_part = line.split(":")
        game_id = int(info_part[0].split(" ")[1].strip())
        attempts = self.get_attempts(info_part[1].strip())
        return Game(game_id, attempts)
        
    def get_attempts(self, attempts_info: str) -> list[dict[str: int]]:
        attempts = attempts_info.split(";")
        attempts_result = list()
        for attempt in attempts:
            colors = attempt.strip().split(",")
            colors_count = dict()
            for color in colors:
                color = color.split()
                colors_count[color[1]] = int(color[0])
            attempts_result.append(colors_count)
        return attempts_result

app = Main()
print(app.run("day2/task2/values.txt"))