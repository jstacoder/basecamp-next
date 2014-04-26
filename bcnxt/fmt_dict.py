# coding: utf-8
def fmt(d):
    rng = len(d)
    res = []
    k = d.keys()
    while rng != 0:
        for x in range(len(d)):
            res.append(k[x])
            if not type(d[k[x]]) == dict:
                res.append(d[k[x]])
            else:
                fmt(d[k[x]])
        rng -= 1
    return res
    
        
