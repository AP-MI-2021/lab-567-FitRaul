from Domain.carte import get_gen
from Logic.modify_title_by_gen import genres_list


def distinct_titles(carti):
    """
    Returneaza numarul de titluri pentru fiecare gen din carti
    :param carti: lista cu carti
    :return: nt: lista cu numarul de titluri pentru fiecare gen
              g: lista de genuri distincte
    """
    genuri=genres_list(carti)
    nt=[]
    g=[]
    for gen in genuri:
        n=0
        for carte in carti:
            if gen == get_gen(carte):
                n+=1

        nt.append(n)
        g.append(gen)
    return nt,g