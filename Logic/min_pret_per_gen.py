from Domain.carte import get_gen, get_pret


def get_min_pret_per_gen(lst_carti):
    """
    :param lst_carti:lista de carti
    :return:un dictionar in care cheia este genul si valoarea este cartea cu pretul minim pentru acel gen
    """
    result={} #result[x]=cartea cu pretul minim din genul x
    for carte in lst_carti:
        gen = get_gen(carte)
        pret = get_pret(carte)
        if gen not in result:
            result[gen] = carte
        else:
            if pret < get_pret(result[gen]):
                result[gen] = carte

    return result