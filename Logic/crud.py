from Domain.carte import creeaza_carte, get_id

def inverse_create(lst_carti, id_carte):
    new_carti = []
    for carte in lst_carti:
        if get_id(carte) != id_carte:
            new_carti.append(carte)
    return new_carti


def create(lst_carti,
           id_carte: int , titlu, gen, pret, tip_reducere,undo_list: list,redo_list: list):
    """
    :param lst_carti: lista de carti.
    :param id_carte:id-ul cartii
    :param titlu:titlul cartii
    :param gen:genul cartii
    :param pret:pretul cartii
    :param tip_reducere:tipul de reducere al cartii
    :param redo_list:
    :param undo_list:
    :return: o noua lista formata din lst_carti si noua carte adaugata.
    """
    if read(lst_carti, id_carte) is not None:
        raise ValueError(f'Exista deja o carte cu id-ul {id_carte}')


    carte = creeaza_carte(id_carte, titlu, gen, pret, tip_reducere)
    # undo_list.append(lst_carti) ineficient
    undo_list.append(
        (lambda lst: inverse_create(lst, id_carte),
         lambda lst: lst.append(carte))
    )

    redo_list.clear()

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




def update(lst_carti, new_carte, undo_list, redo_list):
    """
    Actualizeaza o carte.
    :param lst_carti: lista de carti.
    :param new_carte: cartea care se va actualiza - id-ul trebuie sa fie unul existent.
    :param undo_list:
    :param redo_list:
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

    undo_list.append(lst_carti)
    redo_list.clear()

    return new_carti


def delete(lst_carti, id_carte: int, undo_list, redo_list):
    """
    :param lst_carti:
    :param id_carte:
    :param undo_list:
    :param redo_list:
    :return: o lista de carti fara cartea cu id-ul id_carte.
    """

    if read(lst_carti, id_carte) is None:
        raise ValueError(f'Nu exista o carte cu id-ul {id_carte} pe care sa o stergem.')

    new_carti = []
    for carte in lst_carti:
        if get_id(carte) != id_carte:
            new_carti.append(carte)

    undo_list.append(lst_carti)
    redo_list.clear()

    return new_carti


