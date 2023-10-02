#!/usr/bin.python3
"""
Module that prints 2 new lines
after . or ? or :
"""


def text_indentation(text):
    """function for identation"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    ident_chars = [".", "?", ":"]
    prev_ident = 0
    text2 = text.strip()
    for i in range(len(text2)):
        if text2[i] in ident_chars:
            prev_ident = 1
            print(text2[i], end="\n\n")
        elif prev_ident == 1 and text2[i] == " ":
            i += 1
        else:
            prev_ident = 0
            print(text2[i], end="")
