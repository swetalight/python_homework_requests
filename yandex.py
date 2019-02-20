import os
import requests
import inspect

API_KEY = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'


def translate_it(text, to_lang, from_lang):
    """
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]

    :param to_lang:
    :return:
    """

    params = {
        'key': API_KEY,
        'text': text,
        'lang': '{}-{}'.format(from_lang, to_lang)
    }

    response = requests.get(URL, params=params)
    json_ = response.json()
    return ''.join(json_['text'])


def fun_translate_file(path_file, name_file, to_lang, from_lang):
    dirname = os.path.dirname(os.path.abspath(inspect.stack()[0][1]))
    filename = os.path.join(dirname, path_file, name_file)

    with open(filename, encoding='utf-8') as datafile:
        f = datafile.read()
        rezult = translate_it(f, to_lang, from_lang)
        print(rezult)
    return rezult


def fun_save_result(path_name_save, name_file_save, path_file, name_file, to_lang, from_lang):
    dirname = os.path.dirname(os.path.abspath(inspect.stack()[0][1]))
    filename = os.path.join(dirname, path_name_save, name_file_save)

    translate = fun_translate_file(path_file, name_file, to_lang, from_lang)

    with open(filename, 'w') as datafile:
        f = datafile.write(translate)
    return 'Результат сохранен в файле {}'.format(filename)


if __name__== '__main__':

    to_lang = 'ru'
    print('====================================================================')
    print('==============перевод с французкого=================================')
    print('====================================================================')
    print(fun_save_result('files','tra_fr.txt','files','FR.txt', to_lang, 'fr'))
    print('=====================================================================')

    print('====================================================================')
    print('==============перевод с испанского =================================')
    print('====================================================================')
    print(fun_save_result('files', 'tra_esp.txt', 'files', 'ES.txt', to_lang, 'es'))
    print('=====================================================================')

    print('====================================================================')
    print('==============перевод с немецкого= =================================')
    print('====================================================================')
    print(fun_save_result('files', 'tra_de.txt', 'files', 'DE.txt', to_lang, 'de'))
    print('=====================================================================')