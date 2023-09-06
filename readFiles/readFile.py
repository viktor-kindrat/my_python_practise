import string


def word_analise(path):
    with open(path, "r", encoding="utf-8") as text_file:
        trans = str.maketrans("", "", string.punctuation)
        word_list = text_file.read().translate(trans).split(" ")

        res = {}
        for el in word_list:
            if el in res:
                res[el] += 1
            else:
                res[el] = 1

        return res


print(word_analise("files/lorem.txt"))
