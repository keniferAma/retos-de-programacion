
# funciones #
def sumar(number_1, number_2):
    return number_1 + number_2

def login(username, password):
    if username == 'keniferamariles' and password == 123456:
        return True
    else:
        return False
    
class LanguageModel:

    @classmethod
    def get_languages(cls):
        languages = ['python', 'kotlin', 'javascript', 'swift']
        return languages

