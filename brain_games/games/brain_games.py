import prompt
# from brain_games.cli import welcome_user


# def get_user_name():
#     user_name = prompt.string('', empty=True)
#     return user_name if user_name is not None else 'Anonymous'

def main():
    print('/Welcome to the Brain Games!/', flush=True)
    # text = '/Welcome to the Brain Games!/\n/May I have you name?/'
    text = '/May I have you name?/'
    print(text, flush=True)
    user_name = prompt.string(
        empty=True,
    ) or 'Anonymous'
    print(f'/Hello, {user_name}!/', flush=True)


if __name__ == "__main__":
    main()
