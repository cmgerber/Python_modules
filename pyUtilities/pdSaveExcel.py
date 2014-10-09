import pandas as pd
from pandas import ExcelWriter

def save_xls_name(list_dfs, xls_path, sheet_name):
    '''save function that takes a list as input to name sheets.'''

    #remove ascii characters from dataframes for saving
    for df in list_dfs:
        df.index = remove_non_ascii(df.index)
        for col in df.columns:
        df[col] = remove_non_ascii(df[col])

    #save the df's to an excel file
    writer = ExcelWriter(xls_path)
    for n, df in enumerate(list_dfs):
        df.to_excel(writer, sheet_name[n])
    writer.save()


def remove_non_ascii(col):
    '''remove ascii for saving to excel'''
    new_index = []
    for name in col:
        try:
            for letter in name:
                if ord(letter) > 128:
                    name = name.replace(letter, '')
        except:
            pass
        new_index.append(name)
    return new_index
