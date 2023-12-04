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
                if not self.check_color_amounts(attempt, configuration):
                    return False
            else:
                return False
        return True

    def check_color_intersection(self, attempt: dict[str: int], configuration: dict[str: int]) -> bool:
        # attempt_set = set(attempt.keys())
        # configuration_set = set(configuration.keys())
        for color in attempt:
            if color not in configuration:
                return False
        return True
    
    # color amount in any attempt has to be less than or equal to the one in configuration
    def check_color_amounts(self, attempt: dict[str: int], configuration: dict[str: int]):
        for color in attempt:
            if configuration.get(color) < attempt.get(color):
                return False
        return True
    
    def __str__(self):
        return str(self.id) + " " + str(self.attempts)
    
    
class Main():
    # returns sum of ids of possible games
    def run(self, path: str) -> int:
        lines = self.read_lines(path)
        games = self.get_games(lines)
        
        if DEBUGGING:
            for game in games:
                print(f'Game {game.id}: is possible: {game.is_game_possible(CONFIGURATION)}')
                
        return sum([game.id for game in games if game.is_game_possible(CONFIGURATION)])
    
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
print(app.run("day2/task1/values.txt"))