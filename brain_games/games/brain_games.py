import prompt
# from brain_games.cli import welcome_user


def get_user_name():
    user_name = prompt.string(
        # 'Welcome to the Brain Games!\n'
        'May I have you name? ', empty=True
    )
    return user_name if user_name is not None else 'Anonymous'


def main():
    print('Welcome to the Brain Games!')
    user_name = prompt.string(
        'May I have you name? ',
        empty=True,
    )
    user_name = get_user_name()
    print(f'Hello, {user_name}!')


if __name__ == "__main__":
    main()
