#!/usr/bin/env python3
import prompt


def welcome_user():
    name = prompt.string('May I have you name?\n')
    print(f'Hello, {name}!')
