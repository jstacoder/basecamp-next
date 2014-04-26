import HTML

def process_data(data):
    rtn = []
    tmp = []
    tbls = [HTML.Table(header_row=['basecamp data',''])]
    for itm in data:
        if type(data[itm]) == dict:
            tbls.append(HTML.Table(header_row=[itm,'']))
            for x in data[itm]:
                tbls[len(tbls)-1].rows.append(x,data[itm[x]])
        else:
            tbls[0].append((itm,data[data.index(itm)]))
    return tbls
