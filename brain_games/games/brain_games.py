import prompt
# from brain_games.cli import welcome_user


# def get_user_name():
#     user_name = prompt.string('', empty=True)
#     return user_name if user_name is not None else 'Anonymous'

def main():
    print('/Welcome to the Brain Games!/')
    text = '/May I have your name?/'
    user_name = prompt.string(
        prompt=text,
        empty=True,
    ) or 'Anonymous'
    print(f'/Hello, {user_name}!/')


if __name__ == "__main__":
    main()
