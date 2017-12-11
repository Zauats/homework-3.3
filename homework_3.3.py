import requests

def translate_it(text = None, lang_1 = None, lang_2 = 'ru'):

    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    key = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'
    params = {
        'key': key,
        'lang': "{}{}{}".format(lang_1,"-",lang_2),
        'text': text,
    }
    response = requests.get(url, params=params).json()
    return ' '.join(response.get('text', []))



language_1 = input("введите язык, с которого вы будете переводить: ").lower()
language_2 = input("Введите язык на который вы будете переводить: ").lower()


def file_name():
    word = input("введите переводимый текст или нажмите '1' для того что бы ввести файл: ")
    if word == "1":
        file_name = input("введите имя файла")
        with open(file_name) as f:
            file_information = f.read()
            return file_information
    else:
        return word


text_translate = translate_it(file_name(), language_1, language_2)

with open("translate.txt", "w", encoding= "UTF8") as file:
    a = file.write(text_translate)
