from Domain.carte import get_id, get_pret, get_tip_reducere, get_gen, get_titlu, creeaza_carte


def reducere_pret_pentru_nume(vanzari,undo_list: list, redo_list: list):
    new_vanzari = []
    for vanzare in vanzari:
        if get_tip_reducere(vanzare) == 'silver':
            vanzare_noua = creeaza_carte(get_id(vanzare),
                                           get_titlu(vanzare),
                                           get_gen(vanzare),
                                           get_pret(vanzare) - get_pret(vanzare) * 0.05,
                                           get_tip_reducere(vanzare)
                                           )
            new_vanzari.append(vanzare_noua)
        elif get_tip_reducere(vanzare) == 'gold':
            vanzare_noua = creeaza_carte(get_id(vanzare),
                                           get_titlu(vanzare),
                                           get_gen(vanzare),
                                           get_pret(vanzare) - get_pret(vanzare) * 0.10,
                                           get_tip_reducere(vanzare)
                                           )
            new_vanzari.append(vanzare_noua)
        else:
            new_vanzari.append(vanzare)

    undo_list.append(vanzari)
    redo_list.clear()
    return new_vanzari