import base64

from flask import Flask, request

app = Flask(__name__)


cmd = "print(list(globals())[:-True][:-True][:-True][:-True][:-True][-True])"
def challenge_3(cmd):
    black_char = [
            "'", '"', '.', ',', ' ', '+',
            '__', 'exec', 'eval', 'str', 'import',
            'except', 'if', 'for', 'while', 'pass',
            'with', 'assert', 'break', 'class', 'raise',
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
        ]
    for char in black_char:
        if char in cmd:
            print("black:"+char)
            exit("")

    msg = "success"
    eval(cmd)

challenge_3(cmd)