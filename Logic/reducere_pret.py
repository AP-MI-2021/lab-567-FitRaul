from Domain.carte import  get_pret, creeaza_carte, get_id, get_titlu, get_gen, get_tip_reducere


def reducere_pret_pentru_nume(lst_carti, continut_nume, procentaj, undo_list: list, redo_list: list):
    """

    :param lst_carti:
    :param continut_nume:
    :param procentaj: intre 0 si 100
    :return:
    """

    if not (0 <= procentaj <=100):
        raise ValueError('Procentajul trebuie sa fie intre 0 si 100')
    if continut_nume == '':
        raise ValueError('Textul cautat nu poate fi gol')


    result = []
    for carte in lst_carti:
        if continut_nume in get_titlu(carte):
            pret_nou= get_pret(carte)-(procentaj /100) * get_pret(carte)
            result.append(creeaza_carte(
                get_id(carte),
                get_titlu(carte),
                get_gen(carte),
                pret_nou,
                get_tip_reducere(carte)
            ))
        else:
            result.append(carte)

    undo_list.append(lst_carti)
    redo_list.clear()

    return result

