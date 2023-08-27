import string


def calc_word_frequency(text):
    res = {}
    translator = str.maketrans("", "", string.punctuation)
    words = text.translate(translator).split()

    for el in words:
        if el in res:
            res[el] += 1
        else:
            res[el] = 1
    return res


def calc_symbol_frequency(text):
    res = {}
    for symb in text:
        if symb in res:
            res[symb] += 1
        else:
            res[symb] = 1
    return res


print(
    "\n\nWord analysis:",
    calc_word_frequency(
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Velit euismod in pellentesque massa placerat duis ultricies. Nisl pretium fusce id velit ut tortor. Sit amet facilisis magna etiam tempor. Diam quam nulla porttitor massa id neque aliquam vestibulum morbi. Odio ut sem nulla pharetra diam. Scelerisque in dictum non consectetur a erat nam at. Elit sed vulputate mi sit amet mauris commodo. Turpis tincidunt id aliquet risus. Tincidunt praesent semper feugiat nibh sed. Est ante in nibh mauris. Proin libero nunc consequat interdum varius sit amet. Aliquet nibh praesent tristique magna sit amet. Massa sapien faucibus et molestie ac feugiat sed lectus vestibulum. Mi bibendum neque egestas congue. Augue interdum velit euismod in pellentesque massa placerat. Non quam lacus suspendisse faucibus interdum posuere lorem ipsum dolor. Consectetur adipiscing elit ut aliquam purus sit. Nibh sit amet commodo nulla facilisi nullam. Et malesuada fames ac turpis egestas maecenas pharetra convallis posuere. Suspendisse ultrices gravida dictum fusce ut. Aliquet bibendum enim facilisis gravida neque. Tellus id interdum velit laoreet. Velit sed ullamcorper morbi tincidunt ornare massa. Et ultrices neque ornare aenean euismod. Nec feugiat nisl pretium fusce. A diam sollicitudin tempor id eu nisl. Pretium fusce id velit ut tortor pretium viverra suspendisse. Neque convallis a cras semper auctor neque vitae tempus quam. Velit egestas dui id ornare arcu odio. Cras semper auctor neque vitae tempus quam pellentesque."
    ),
)
print(
    "\n\nSymbol analysis:",
    calc_symbol_frequency(
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Velit euismod in pellentesque massa placerat duis ultricies. Nisl pretium fusce id velit ut tortor. Sit amet facilisis magna etiam tempor. Diam quam nulla porttitor massa id neque aliquam vestibulum morbi. Odio ut sem nulla pharetra diam. Scelerisque in dictum non consectetur a erat nam at. Elit sed vulputate mi sit amet mauris commodo. Turpis tincidunt id aliquet risus. Tincidunt praesent semper feugiat nibh sed. Est ante in nibh mauris. Proin libero nunc consequat interdum varius sit amet. Aliquet nibh praesent tristique magna sit amet. Massa sapien faucibus et molestie ac feugiat sed lectus vestibulum. Mi bibendum neque egestas congue. Augue interdum velit euismod in pellentesque massa placerat. Non quam lacus suspendisse faucibus interdum posuere lorem ipsum dolor. Consectetur adipiscing elit ut aliquam purus sit. Nibh sit amet commodo nulla facilisi nullam. Et malesuada fames ac turpis egestas maecenas pharetra convallis posuere. Suspendisse ultrices gravida dictum fusce ut. Aliquet bibendum enim facilisis gravida neque. Tellus id interdum velit laoreet. Velit sed ullamcorper morbi tincidunt ornare massa. Et ultrices neque ornare aenean euismod. Nec feugiat nisl pretium fusce. A diam sollicitudin tempor id eu nisl. Pretium fusce id velit ut tortor pretium viverra suspendisse. Neque convallis a cras semper auctor neque vitae tempus quam. Velit egestas dui id ornare arcu odio. Cras semper auctor neque vitae tempus quam pellentesque."
    ),
)
