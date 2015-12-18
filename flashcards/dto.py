import json

class Question:
    word = ''
    translation = ''
    correct = False
    
    def __init__(self, word, translation, ):
        self.word = word
        self.translation = translation
    
    def __str__(self):
        return self.word

    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)
    