from brain_games.cli import run_game
from brain_games.generate_random_num import generate_random_num


GAME_NAME = 'brain_progression'
DIGIT_CAPACITY = 100
STEP_BOTTOM_LIMIT = 1
STEP_TOP_LIMIT = 21
MIN_LENGTH = 5
MAX_LENGTH = 10


def generate_quest():
    length = generate_random_num(
        range=(MAX_LENGTH - MIN_LENGTH + 1),
        min_value=MIN_LENGTH,
    )
    new_num = generate_random_num(range=DIGIT_CAPACITY)
    secret_num_position = generate_random_num(range=(length - 1))
    step = generate_random_num(
        min_value=STEP_BOTTOM_LIMIT,
        range=STEP_TOP_LIMIT,
    )
    progression = list(range(new_num, new_num + (step * length), step))
    secret_num = progression[secret_num_position]
    progression[secret_num_position] = '..'
    progression_string = ' '.join([str(el) for el in progression])
    return [str(secret_num), progression_string]


def main():
    run_game(GAME_NAME, generate_quest)


if __name__ == "__main__":
    main()
