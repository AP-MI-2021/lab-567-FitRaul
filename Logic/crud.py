from Domain.carte import creeaza_carte, get_id


def create(lst_carti,
           id_carte: int , titlu, gen, pret, tip_reducere):
    """
    :param lst_carti: lista de carti.
    :param id_carte:id-ul cartii
    :param titlu:titlul cartii
    :param gen:genul cartii
    :param pret:pretul cartii
    :param tip_reducere:tipul de reducere al cartii
    :return: o noua lista formata din lst_carti si noua carte adaugata.
    """
    if read(lst_carti, id_carte) is not None:
        raise ValueError(f'Exista deja o carte cu id-ul {id_carte}')

    carte = creeaza_carte(id_carte, titlu, gen, pret, tip_reducere)
    return lst_carti + [carte]


def read(lst_carti, id_carte: int=None):
    """
    Citeste o carte din "baza de date".
    :param lst_carti: lista de carti
    :param id_carte: id-ul cartii dorite.
    :return: -cartea cu id-ul id_carte daca exista
             -lista cu toate cartile, daca id_carte=None
             -None,daca nu exista o carte cu id_carte
    """
    if not id_carte:
        return lst_carti

    carte_cu_id = None
    for carte in lst_carti:
        if get_id(carte) == id_carte:
            carte_cu_id = carte

    if carte_cu_id:
        return carte_cu_id
    return None




def update(lst_carti, new_carte):
    """
    Actualizeaza o carte.
    :param lst_carti: lista de carti.
    :param new_carte: cartea care se va actualiza - id-ul trebuie sa fie unul existent.
    :return: o lista cu cartea actualizata.
    """

    if read(lst_carti, get_id(new_carte)) is None:
        raise ValueError(f'Nu exista o carte cu id-ul {get_id(new_carte)} pe care sa o actualizam.')

    new_carti = []
    for carte in lst_carti:
        if get_id(carte) != get_id(new_carte):
            new_carti.append(carte)
        else:
            new_carti.append(new_carte)
    return new_carti


def delete(lst_carti, id_carte: int):
    """
    :param lst_carti:
    :param id_carte:
    :return: o lista de carti fara cartea cu id-ul id_carte.
    """

    if read(lst_carti, id_carte) is None:
        raise ValueError(f'Nu exista o carte cu id-ul {id_carte} pe care sa o stergem.')

    new_carti = []
    for carte in lst_carti:
        if get_id(carte) != id_carte:
            new_carti.append(carte)

    return new_carti


