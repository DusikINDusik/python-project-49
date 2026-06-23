from brain_games.engine import games_engine
from brain_games.games.even import is_even

def main():
    games_engine(is_even, 'Answer "yes" if the number is even, otherwise answer "no".')

if __name__ == '__main__':
    main()