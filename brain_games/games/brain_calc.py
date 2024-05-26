from brain_games.cli import run_game
from brain_games.generate_random_num import generate_random_num


GAME_NAME = 'brain_calc'
DIGIT_CAPACITY = 100


def generate_sign():
    math_signs = ['+', '-', '*']
    randomIndex = generate_random_num(min_value=0, range=len(math_signs))
    return math_signs[randomIndex]


def add(a, b):
    return str(a + b)


def substract(a, b):
    return str(a - b)


def multiply(a, b):
    return str(a * b)


calc_functions = {
    '+': add,
    '-': substract,
    '*': multiply,
}


def calc_answer(quest_data):
    [num1, num2, sign] = quest_data
    return calc_functions[sign](num1, num2)


def generate_quest():
    num1 = generate_random_num(range=DIGIT_CAPACITY)
    num2 = generate_random_num(range=DIGIT_CAPACITY)
    sign = generate_sign()
    quest_data = [num1, num2, sign]
    return [calc_answer(quest_data), quest_data]


def main():
    run_game(GAME_NAME, generate_quest)


if __name__ == "__main__":
    main()
