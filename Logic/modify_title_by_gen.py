from Domain.carte import  get_pret,get_gen, creeaza_carte, get_id, get_titlu, get_tip_reducere


def genres_list(carti):
    """
    Returneaza o lista ce contine genurile din vanzari.
    :param carti: lista cu vanzari
    :return: lista cu genuri distincte
    """
    genres=[]
    for carte in carti:
        gen=get_gen(carte)
        if gen not in genres:
            genres.append(gen)
    return genres


def modify_gen_by_title(lst_carti, titlu, undo_list: list, redo_list: list):
    """
    Modifica genul pentru un titlu dat.
    """

    result = []
    for carte in lst_carti:
        if titlu in get_titlu(carte):
            gen_nou = input('Introduceti noul gen: ')
            result.append(creeaza_carte(
                get_id(carte),
                get_titlu(carte),
                gen_nou,
                get_pret(carte),
                get_tip_reducere(carte)
            ))
        else:
            result.append(carte)

    undo_list.append(lst_carti)
    redo_list.clear()

    return result