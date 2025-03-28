def invertir_lista(lista):
    return lista[::-1]

def collatz(i):
    assert i > 0
    while i > 1:
        if i%2 == 0: 
            i /= 2
        else: 
            i = i*3 + 1

def contar_definiciones(my_dict):
    return {k:len(v) for k,v in my_dict.items()}

def cantidad_de_claves_letra(my_dict, start):
    return sum([1 if k.startswith(start) else 0 for k,_ in my_dict.items()])

def propagar(fos):
    index_1 = [i for i, x in enumerate(fos) if x == 1]
    index_neg_1 = [i for i, x in enumerate(fos) if x == -1]
    results = []
    if len(index_neg_1)>0:
        for i, f in enumerate(fos):
            if f != 0:
                results.append(f)
            else:
                min_1 = min([abs(i-i1) for i1 in index_1])
                min_neg_1 = min([abs(i-i_neg_1) for i_neg_1 in index_neg_1])
                if min_1 <= min_neg_1:
                    results.append(1)
                    fos[i] = 1
                    index_1 = [i for i, x in enumerate(fos) if x == 1]
                else:
                    results.append(0)
    else:
        results = [1]*len(fos)
    return results