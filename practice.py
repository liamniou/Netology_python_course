import requests
def translate_it(source_file_path, result_file_path, source_language, result_language='ru'):
    """
    YANDEX translation plugin

    docs: https://tech.yandex.ru/translate/doc/dg/reference/translate-docpage/

    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]

    :param text: <str> text for translation.
    :return: <str> translated text.
    """
    with open(source_file_path, encoding='utf-8') as file:
        url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
        key = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'

        params = {
            'key': key,
            'lang': source_language + '-' + result_language,
            'text': file,
        }
        response = requests.get(url, params=params).json()
        text = (' '.join(response.get('text', []))).replace('\n', '')
        file_for_result = open(result_file_path, 'w')
        file_for_result.write(text)

translate_it('DE.txt', 'DE_result.txt', 'de', 'ru')
translate_it('ES.txt', 'ES_result.txt', 'es', 'ru')
translate_it('FR.txt', 'FR_result.txt', 'fr', 'ru')