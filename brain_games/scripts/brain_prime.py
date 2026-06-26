from brain_games.engine import games_engine
from brain_games.games.prime import is_prime

def main():
    games_engine(is_prime, 'Answer "yes" if given number is prime. Otherwise answer "no".')

if __name__ == '__main__':
    main()