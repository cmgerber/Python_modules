import cPickle as pickle


def save_object(obj, filename):
    '''Use this to save objects as pickles'''
    with open(filename, 'wb') as output:
        pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)


def open_object(obj, filename):
    '''Use this to open pickles'''
    with open(filename, 'rb') as input:
        obj = pickle.load(input)
