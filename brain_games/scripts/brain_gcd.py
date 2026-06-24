from brain_games.engine import games_engine
from brain_games.games.gcd import is_game_gcd

def main():
    games_engine(is_game_gcd, 'Find the greatest common divisor of given numbers.')

if __name__ == '__main__':
    main()