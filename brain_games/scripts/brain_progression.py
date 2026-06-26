from brain_games.engine import games_engine
from brain_games.games.progression import game_progression

def main():
    games_engine(game_progression, 'What number is missing in the progression?')

if __name__ == '__main__':
    main()