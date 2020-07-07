import json
import requests
from html import unescape
from Question import Question

class Quiz():    
    @classmethod
    def get_categories(cls) -> dict:
        with open("quiz_categories.json","r") as readable_file:
            raw_content = readable_file.readline()
            return json.loads(raw_content)
    
    @classmethod
    def get_questions(cls, category: str, amount: int = 10) -> list:
        try:
            api_url = "https://opentdb.com/api.php"
            response = requests.get(f"{api_url}?type=multiple&amount={amount}&category={category}")
            content = json.loads(response.text)
            return content["results"]
        except Exception:
            return []
    
    def __init__(self) -> None:
        self.questions: list = []
        self.score: int = 0

    def add_raw_questions(self, raw_questions: list) -> None:
        for raw_question in raw_questions:
            options = []
            for option in raw_question["incorrect_answers"]:
                options.append(unescape(option))
            
            title = unescape(raw_question["question"])
            answer = unescape(raw_question["correct_answer"])
            options.append(answer)

            question = Question(title, options, answer)
            self.questions.append(question)


