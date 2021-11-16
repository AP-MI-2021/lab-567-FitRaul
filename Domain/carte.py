def creeaza_carte(id_carte: int, titlu, gen, pret, tip_reducere):
    """
    Creeaza o carte.
    :param id_carte: id-ul cartii
    :param titlu:titlul cartii
    :param gen:genul cartii
    :param pret:pretul cartii
    :param tip_reducere:tipul de reducere al cartii
    :return:o carte
    """
    return [
         id_carte,
         titlu,
         gen,
         pret,
         tip_reducere,
    ]

def get_id(carte):
    """
    Getter pentru id-ul cartii.
    :param :
    :return: id-ul cartii date ca parametru.
    """
    return carte[0]


def get_titlu(carte):
    """
       Getter pentru titlul cartii.
       :param : cartea
       :return: titlul cartii date ca parametru.
       """
    return carte[1]


def get_gen(carte):
    return carte[2]


def get_pret(carte):
    return carte[3]


def get_tip_reducere(carte):
    return carte[4]



def get_str(carte):
    return f'Cartea cu id-ul {get_id(carte)}, genul {get_gen(carte)}, titlul {get_titlu(carte)}, pretul {get_pret(carte)}, reducerea de tipul {get_tip_reducere(carte)}'

