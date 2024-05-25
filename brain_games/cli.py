#!/usr/bin/env python3
import prompt


ROUNDS_LIMIT = 3


def ask_question(question_text):
    return prompt.string(f'{question_text}\n')


def get_user_name():
    user_name = prompt.string('May I have you name?\n', empty=True)
    return user_name if user_name is not None else 'Anonymous'


def welcome_user():
    user_name = get_user_name()
    print(f'Hello, {user_name}!')
    return user_name


def generate_brain_even_text(num):
    description = 'Answer "yes" if the number is even, otherwise answer "no".\n'
    task = f'Question: {num}\n'
    return [description, task]


def generate_brain_calc_text(quest_data):
    [num1, num2, sign] = quest_data
    description = 'What is the result of the expression?\n'
    task = f'Question: {num1} {sign} {num2}\n'
    return [description, task]


def generate_brain_gcd_text(quest_data):
    [num1, num2] = quest_data
    description = 'Find the greatest common divisor of given numbers.\n'
    task = f'Question: {num1} {num2}\n'
    return [description, task]


def generate_brain_prime_text(num):
    description = 'Answer "yes" if given number is prime.'.join(
        ' Otherwise answer "no".\n'
    )
    task = f'Question: {num}\n'
    return [description, task]


def generate_brain_progression_text(questString):
    description = 'What number is missing in the progression?\n'
    task = f'Question: {questString}\n'
    return [description, task]


text_generators = {
    'brain_even': generate_brain_even_text,
    'brain_calc': generate_brain_calc_text,
    'brain_gcd': generate_brain_gcd_text,
    'brain_prime': generate_brain_prime_text,
    'brain_progression': generate_brain_progression_text,
}


def generate_question_text(game_name, quest_data):
    text_generator = text_generators[game_name]
    [description, task] = text_generator(quest_data)
    text = 'Your answer: '
    full_question = f'{description}{task}{text}'
    short_question = f'{task}{text}'
    return [full_question, short_question]


def run_game(game_name, quest_generator):
    user_name = welcome_user()
    if not quest_generator:
        return
    for round_index in range(ROUNDS_LIMIT):
        last_round_index = ROUNDS_LIMIT - 1
        [correct_answer, quest_data] = quest_generator()
        [full_text, short_text] = generate_question_text(
            game_name,
            quest_data
        )

        if round_index == 0:
            user_answer = ask_question(full_text)
        else:
            user_answer = ask_question(short_text)

        if (user_answer == correct_answer):
            print('Correct!')
            if (round_index == last_round_index):
                print(f'Congratulations, {user_name}!')
        else:
            print(
                f'"{user_answer}" is wrong answer ;(.'
                f' Correct answer was "{correct_answer}"'
            )
            print(f'Let\'s try again, {user_name}!')
            break
