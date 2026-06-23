from brain_games.engine import games_engine
from brain_games.games.calc import calculate_game

def main():
    games_engine(calculate_game, "What is the result of the expression?")

if __name__ == '__main__':
    main()