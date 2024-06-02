import prompt
# from brain_games.cli import welcome_user


# def get_user_name():
#     user_name = prompt.string('', empty=True)
#     return user_name if user_name is not None else 'Anonymous'


def main():
    text = '/Welcome to the Brain Games!/\n/May I have you name?/'
    user_name = prompt.string(
        prompt=text,
        empty=True,
    ) or 'Anonymous'
    print(f'/Hello, {user_name}!/')


if __name__ == "__main__":
    main()
