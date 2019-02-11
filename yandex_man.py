import os
import requests

API_KEY = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'


class MyManager():

    def __init__(self, path_file_save, name_file_save, path_file, name_file, to_lang):
        self.name_file = name_file
        self.path_file = path_file
        self.to_lang = to_lang
        self.path_file_save = path_file_save
        self.name_file_save = name_file_save

    def __enter__(self):

        self.read_file = self.fun_translate_file( self.path_file, self.name_file)
        self.translate = self.translate_it(self.read_file, self.to_lang)
        self.save_file = self.fun_save_result(self.path_file_save, self.name_file_save, self.translate)

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


    def fun_translate_file(self, path_file, name_file):
        path = path_file
        os.chdir(path)

        file = name_file
        with open(file, encoding='utf-8') as datafile:
            f = datafile.read()
            #print(f)
        return f

    def translate_it(self, text, to_lang):
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

    def fun_save_result(self, path_file_save, name_file_save, translate):
        path = path_file_save
        os.chdir(path)
        file = name_file_save


        with open(file, 'w') as datafile:
            f = datafile.write(translate)

        return f

if __name__ == '__main__':
    with MyManager('C:/sweta/txt', 'tra_fr.txt', 'C:/sweta/txt', 'FR.txt', 'fr-ru') as mymanager:
        print('====================================================================')
        print('==============перевод с французкого=================================')
        print('====================================================================')
        mymanager.read_file
        mymanager.translate
        mymanager.save_file

        print('====================================================================')

    with MyManager('C:/sweta/txt', 'tra_esp.txt', 'C:/sweta/txt', 'ES.txt', 'es-ru') as mymanager_esp:
        print('====================================================================')
        print('==============перевод с испанского==================================')
        print('====================================================================')
        mymanager_esp.read_file
        mymanager_esp.translate
        mymanager_esp.save_file

        print('====================================================================')

    with MyManager('C:/sweta/txt', 'tra_de.txt', 'C:/sweta/txt','DE.txt', 'de-ru') as mymanager_de:
        print('====================================================================')
        print('==============перевод с немецкого===================================')
        print('====================================================================')
        mymanager_de.read_file
        mymanager_de.translate
        mymanager_de.save_file

        print('====================================================================')