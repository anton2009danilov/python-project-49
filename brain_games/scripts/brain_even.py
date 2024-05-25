#!/usr/bin/env python3
import random
from brain_games.cli import run_game


GAME_NAME = 'brain_even'
DIGIT_CAPACITY = 1000


def is_even(num):
    return num % 2 == 0


def calc_answer(num):
    return 'yes' if is_even(num) else 'no'


def generate_random_num(minValue=1, range=1):
    return random.randrange(minValue, minValue + range)


def generate_quest():
    num = generate_random_num(range=DIGIT_CAPACITY)
    return [calc_answer(num), num]


def main():
    run_game(GAME_NAME, generate_quest)


if __name__ == "__main__":
    main()
