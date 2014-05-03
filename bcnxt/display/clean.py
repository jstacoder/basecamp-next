# coding: utf-8
def clean_itm(itm):
    out = list(itm)
    for i in range(len(out)):
        if out[i] == '_':
            out[i] = ' '
    return ''.join(map(str,out))
