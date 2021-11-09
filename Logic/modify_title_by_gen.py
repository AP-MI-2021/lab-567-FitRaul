from Domain.carte import  get_pret, creeaza_carte, get_id, get_titlu, get_tip_reducere


def modify_gen_by_title(lst_carti, titlu, undo_list: list, redo_list: list):
    """
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