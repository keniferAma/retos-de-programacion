"""/*
 * EJERCICIO:
 * Crea una función que se encargue de sumar dos números y retornar
 * su resultado.
 * Crea un test, utilizando las herramientas de tu lenguaje, que sea
 * capaz de determinar si esa función se ejecuta correctamente.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un diccionario con las siguientes claves y valores:
 * "name": "Tu nombre"
 * "age": "Tu edad"
 * "birth_date": "Tu fecha de nacimiento"
 * "programming_languages": ["Listado de lenguajes de programación"]
 * Crea dos test:
 * - Un primero que determine que existen todos los campos.
 * - Un segundo que determine que los datos introducidos son correctos.
 */"""

from piedra_papel_tijera import combinations
from functiones_de_testeo import sumar, login, LanguageModel
import pytest

@pytest.mark.parametrize( # When testing multiple parameters
        'input_x, input_y, input_z, expected',
        [
            (('S', 'R'), ('S', 'R'), ('S', 'R'), 'player 2'), # passing the parameters among tuples.
            (('S', 'R'), ('S', 'P'), ('R', 'R'), 'player 2'),
            (('R', 'S'), ('R', 'S'), ('R', 'S'), 'Player 1'),
        ]   
)
def test_combinations(input_x, input_y, input_z, expected):
    assert combinations([input_x, input_y, input_z]) == expected


def test_sumar_function():
    assert sumar(1, 2) == 3


def test_login():
    assert login('keniferamariles', 123456) # si es true, entonces no es necesario == True

def test_login_fails():
    assert not login('alejandro', 123)


def test_get_languages_not_none():
    """test the get_language method has values"""
    languages = LanguageModel.get_languages()
    assert languages != None

def test_every_item_in_get_languages_is_greater_than_zero():
    for language in LanguageModel.get_languages():
        assert len(language) > 0



# Optional challenge #
        
information = {
    'name': 'kenifer',
    'surname': 'amariles',
    'birth_date': '08/04/1993',
    'programming_languages': ['python', 'typescript', 'javascript']
}


def test_every_field_exists():
    for key, value in information.items():
        assert key in ['name', 'surname', 'birth_date', 'programming_languages']
        

def test_every_value_is_correct():
    for key, value in information.items():
        assert value in ['kenifer', 'amariles', '08/04/1993', ['python', 'typescript', 'javascript']]
        