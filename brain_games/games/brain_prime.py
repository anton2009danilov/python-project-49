import math
from brain_games.cli import run_game
from brain_games.generate_random_num import generate_random_num


GAME_NAME = 'brain_prime'
DIGIT_CAPACITY = 100


def is_prime(num):
    MIN_PRIME_NUM = 2
    if num <= 1:
        return False
    if num == MIN_PRIME_NUM:
        return True

    MAX_PRIME_NUM = math.floor(num / 2)
    for divider in range(MIN_PRIME_NUM, MAX_PRIME_NUM + 1):
        if num % divider == 0:
            return False
    return True


def calc_answer(num):
    return 'yes' if is_prime(num) else 'no'


def generate_quest():
    num = generate_random_num(range=DIGIT_CAPACITY)
    return [calc_answer(num), str(num)]


def main():
    run_game(GAME_NAME, generate_quest)


if __name__ == "__main__":
    main()
