from Domain.carte import get_pret


def ascending_prices(carti):
    """
    creeaza o lista ce contine preturile asezate in ordine crescatoare
    :param carti: lista cartilor
    :return: lista cu preturile asezate in ordine crescatoare
    """
    prices=[]
    for carte in carti:
        price=get_pret(carte)
        prices.append(price)
    prices.sort()
    return prices

def sort_ascending(carti,undo_list,redo_list):
    """
    Lista cu cartile ordonate crescator dupa pret, pastrandu-si id-ul initial
    :param carti: lista cartilor
    :return:lista cartilor ordonate crescator dupa pret
    """
    prices=ascending_prices(carti)
    carti_ordonate=[]
    i=0
    while i < len(prices):
        for carte in carti:
            if i<len(prices) and get_pret(carte) == prices[i]:
                carti_ordonate.append(carte)
                i+=1
    undo_list.append(carti)
    redo_list.clear()
    return carti_ordonate