import string

with open("files/lorem.txt", "r", encoding="utf-8") as text_file: 
    trans = str.maketrans("", "", string.punctuation)
    wodrList = text_file.read().translate(trans).split(" ")

    res = {}
    for el in wodrList:
        if (el in res): 
            res[el] += 1
        else: 
            res[el] = 1

    print("\n\nWord analisys", res, sep=": \n")