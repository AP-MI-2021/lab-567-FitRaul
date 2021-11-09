from Domain.carte import creeaza_carte, get_pret, get_id
from Logic.crud import create
from Logic.reducere_pret import reducere_pret_pentru_nume
from Logic.min_pret_per_gen import get_min_pret_per_gen


def test_reducere_pret():
    carte1 = creeaza_carte("1", "Tom Sawyer", "actiune", 50, "silver")
    carte2 = creeaza_carte("2", "La rascruce de vanturi", "roman", 60, "gold")
    lista = []
    lista.append(carte1)
    lista.append(carte2)
    reducere_pret_pentru_nume(lista,"Tom Sawyer",10, [], [])
    reducere_pret_pentru_nume(lista, "La rascruce de vanturi", 10, [], [])

    assert get_pret(lista[0]) == 45
    assert get_pret(lista[1]) == 54



def test_min_pret_per_gen():
    lista = create()
    rezultat = get_min_pret_per_gen(lista)

    assert rezultat["actiune"] == 110
    assert rezultat["drama"] == 150
    assert rezultat["horror"] == 100


def test_all():
    test_reducere_pret()
    test_min_pret_per_gen()
