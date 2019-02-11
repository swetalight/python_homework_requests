import os
import requests

API_KEY = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'


def fun_translate_file(path_file,name_file,to_lang):
    path = path_file
    os.chdir(path)

    file=name_file
    with open(file, encoding='utf-8') as datafile:
        f = datafile.read()
        rezult = translate_it(f,to_lang)
        print(rezult)
    return rezult

def translate_it(text, to_lang):
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
        'lang': to_lang,
    }

    response = requests.get(URL, params=params)
    json_ = response.json()
    return ''.join(json_['text'])

def fun_save_result(path_file_save,name_file_save,path_file,name_file,to_lang):
    path = path_file_save
    os.chdir(path)
    file = name_file_save
    translate = fun_translate_file(path_file, name_file, to_lang)

    with open(file, 'w') as datafile:
        f = datafile.write(translate)


if __name__== '__main__':
    print('====================================================================')
    print('==============перевод с французкого=================================')
    print('====================================================================')
    fun_save_result('C:/sweta/txt','tra_fr.txt','C:/sweta/txt','FR.txt','fr-ru')
    print('=====================================================================')

    print('====================================================================')
    print('==============перевод с испанского =================================')
    print('====================================================================')
    fun_save_result('C:/sweta/txt', 'tra_esp.txt', 'C:/sweta/txt', 'ES.txt', 'es-ru')
    print('=====================================================================')

    print('====================================================================')
    print('==============перевод с немецкого= =================================')
    print('====================================================================')
    fun_save_result('C:/sweta/txt', 'tra_de.txt', 'C:/sweta/txt', 'DE.txt', 'de-ru')
    print('=====================================================================')