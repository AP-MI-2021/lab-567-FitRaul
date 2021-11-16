from Domain.carte import  get_pret
from Logic.reducere_pret import reducere_pret_pentru_nume
from Logic.crud import create,getById
from Logic.min_pret_per_gen import get_min_pret_per_gen
from Logic.title_count_each_genre import distinct_titles


def test_reducere_pret():
    lista = []
    lista = create(lista, 1, 'In Search of Lost Time', 'actiune', 120, 'silver')
    lista = create(lista, 2, 'Tom Sawyer', 'actiune', 120, 'gold')


    lista = reducere_pret_pentru_nume(lista)

    assert get_pret(getById(1, lista)) == 124
    assert get_pret(getById(2, lista)) == 108



def testpretMin():
    lista = []
    lista = create(lista, 1, 'In Search of Lost Time', 'actiune', 100, 'silver')
    lista = create(lista, 2, 'In Search of Lost ', 'actiune', 150, 'silver')
    lista = create(lista, 3, 'In Search of ', 'horror', 120, 'silver')
    lista = create(lista, 4, 'In Search  ', 'horror', 110, 'silver')


    rezultat=get_min_pret_per_gen(lista)

    assert len(rezultat) == 3
    assert rezultat["actiune"] == 100
    assert rezultat["horror"] == 110





def testnumarTitluri():
    lista=[]
    lista = create(lista, 1, 'In Search of Lost Time', 'actiune', 100, 'silver')
    lista = create(lista, 2, 'In Search of Lost Time', 'drama', 100, 'silver')


    rezultat=distinct_titles(lista)

    assert rezultat["actiune"] == 1
    assert rezultat["drama"] == 1