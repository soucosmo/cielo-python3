
import json
from future.utils import integer_types


class ObjectJSON(object):

    def toJSON(self):

        dicionary = json.loads(json.dumps(self, default=lambda o: o.__dict__))

        dicionary = remove_none(dicionary)

        dicionary = process_name_key(dicionary)

        return json.dumps(dicionary, indent=2)

    def prepare(self):
        pass

    def __getattribute__(self, attribute):

        if attribute == '__dict__':
            self.prepare()

        return object.__getattribute__(self, attribute)


def process_name_key(dictionary):

    if not isinstance(dictionary, dict):
        return dictionary

    newDictionary = {}

    for key in dictionary:
        newDictionary[capitalize_key(key)] = process_name_key(dictionary[key])

    return newDictionary

def capitalize_key(key):
    parts = key.split('_')

    newParts = []
    for part in parts:
        newParts.append(part.capitalize())

    return ''.join(newParts)

def remove_none(dado):

    if isinstance(dado, dict):
        return remove_none_dict(dado)
    elif isinstance(dado, list):
        return remove_none_list(dado)

    return dado

def remove_none_dict(obj):
    retorno = {}
    for chave in obj:
        valor = obj[chave]
        types = integer_types + (float, complex)
        if valor or isinstance(valor, types):
            retorno[chave] = remove_none(valor)

    return retorno

def remove_none_list(lista):
    resposta = []
    for linha in lista:
        valor = remove_none(linha)
        resposta.append(valor)

    return resposta
