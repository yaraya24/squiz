import random

class Question():
    def __init__(self, title: str, options: list, answer: str) -> None:
        self.title = title
        self.answer = answer

        random.shuffle(options)
        self.options = options

    def is_correct(self, answer: str) -> bool:
        return self.answer == answer