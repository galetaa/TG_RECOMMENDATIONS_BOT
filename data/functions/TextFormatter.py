from nltk.corpus import stopwords
import pymorphy2


def is_not_punctuation(symbol: str):
    acceptable_symbols = set(
        'абвгдеёжзийклмнопрстуфхцчшщъыьэюяabcdefghijklmnopqrstuvwxyz \n')

    if symbol in acceptable_symbols:
        return True
    return False


def formate_text(text: str):
    pymorph = pymorphy2.MorphAnalyzer()
    stoppers = set(stopwords.words('russian'))

    text_list = ''.join(filter(is_not_punctuation, text.lower())).split()
    result_words = [pymorph.parse(word)[0].normal_form for word in
                    text_list if word not in stoppers]
    return result_words