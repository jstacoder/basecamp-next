# coding: utf-8
import HTML

def process_bc_person(person):
    res = [HTML.Table(header_row=['info for {}'.format(person['name']),''])]
    k = person.keys()
    for itm in k:
        if type(person[itm]) == dict:
            res.append(HTML.Table(header_row=[itm,'']))
            for x in person[itm]:
                res[len(res)-1].rows.append((x,person[itm][x]))
        else:
            res[0].rows.append((itm,person[itm]))
    return '\n<br />'.join(map(str,res))
