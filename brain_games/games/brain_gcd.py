import math
from brain_games.cli import run_game
from brain_games.generate_random_num import generate_random_num


GAME_NAME = 'brain_gcd'
DIGIT_CAPACITY = 101


def find_biggest_common_divider(num1, num2):
    max_divider = num1 if num1 >= num2 else num2

    if num1 % max_divider == 0 and num2 % max_divider == 0:
        return str(max_divider)

    max_divider = math.floor(max_divider / 2)
    MIN_DIVIDER = 1
    STEP = -1

    for divider in range(max_divider, MIN_DIVIDER - STEP, STEP):
        if num1 % divider == 0 and num2 % divider == 0:
            return str(divider)
    return str(MIN_DIVIDER)


def calc_answer(quest_data):
    [num1, num2] = quest_data
    return find_biggest_common_divider(num1, num2)


def generate_quest():
    num1 = generate_random_num(range=DIGIT_CAPACITY)
    num2 = generate_random_num(range=DIGIT_CAPACITY)
    quest_data = [num1, num2]
    return [calc_answer(quest_data), quest_data]


def main():
    run_game(GAME_NAME, generate_quest)


if __name__ == "__main__":
    main()
