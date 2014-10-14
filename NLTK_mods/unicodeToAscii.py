import unicodedata


def norm_unicode(text):
    '''this function takes in a list of strings, and
    normalizes each word in each string from unicode
    characters to equivalent (or closest) ascii
    characters'''
    text_ascii = []
    for doc in text:
        re_combine = []
        for word in doc.split():
            word = unicodedata.normalize('NFKD', word)
            re_combine.append(word)
        text_ascii.append(' '.join(re_combine))
    return text_ascii
