from Domain.carte import get_id, get_pret, get_tip_reducere, get_gen, get_titlu, creeaza_carte


def reducere_pret_pentru_nume(lst_carti, continut_nume, procentaj, undo_list: list, redo_list: list):
    """
    Aplica o reducere unei carti in functie de nume
    :param lst_carti:lista cartilor
    :param continut_nume:stringul cautat in nume pentru reducerea preturilor
    :param procentaj: intre 0 si 100
    :return:o lista cu noile preturi
    """


    result = []
    for carte in lst_carti:
        if continut_nume in get_titlu(carte):
            if procentaj in get_tip_reducere(carte) and procentaj=='silver':
                pret_nou = get_pret(carte) - (5 / 100) * get_pret(carte)
                result.append(creeaza_carte(
                    get_id(carte),
                    get_titlu(carte),
                    get_gen(carte),
                    pret_nou,
                    get_tip_reducere(carte)
                ))

    for carte in lst_carti:
        if continut_nume in get_titlu(carte):
            if procentaj in get_tip_reducere(carte) and procentaj=='gold':
                pret_nou = get_pret(carte) - (10 / 100) * get_pret(carte)
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
