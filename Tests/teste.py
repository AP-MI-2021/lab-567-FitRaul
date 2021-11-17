from Domain.carte import  get_pret,get_tip_reducere,get_titlu,get_gen
from Logic.crud import create
from Logic.min_pret_per_gen import get_min_pret_per_gen
from Logic.title_count_each_genre import distinct_titles
from Domain.carte import creeaza_carte
from Logic.reducere_pret import reducere_pret_pentru_nume
from Logic.modify_title_by_gen import modify_gen_by_title
from Logic.sort_ascending import sort_ascending

def test_reducere_pret():
    vanzari = get_data()
    new_vanzari = reducere_pret_pentru_nume(vanzari, [], [])
    for i in range(0, len(vanzari)):
        if get_tip_reducere(vanzari[i]) != 'none':
            assert get_pret(vanzari[i]) != get_pret(new_vanzari[i])



def test_modificare_gen():
    vanzari = get_data()
    new_vanzari = modify_gen_by_title(vanzari, 'Moara cu noroc',[],[])
    for i in range(0, len(vanzari)):
        if get_titlu(vanzari[i]) == 'Moara cu noroc':
            assert get_gen(vanzari[i]) != get_gen(new_vanzari[i])



def test_pret_min():
    lista = []
    undo_list=[]
    redo_list=[]
    lista = create(lista, 1, 'In Search of Lost Time', 'actiune', 100, 'silver',undo_list,redo_list)
    lista = create(lista, 2, 'In Search of Lost ', 'actiune', 150, 'silver',undo_list,redo_list)
    lista = create(lista, 3, 'In Search of ', 'horror', 120, 'silver',undo_list,redo_list)
    lista = create(lista, 4, 'In Search  ', 'horror', 110, 'silver',undo_list,redo_list)


    rezultat=get_min_pret_per_gen(lista)

    assert rezultat['actiune'] == 100
    assert rezultat['horror'] == 110


def test_titles_count_each_genre():
    vanzari=get_data()
    nt,g= distinct_titles(vanzari)
    assert nt[0] == 1
    assert g[0] == 'g1'
    assert nt[1] == 1
    assert g[1] == 'g2'


def test_sort_ascending():
    vanzari=get_data()
    vanzari_ordonate=sort_ascending(vanzari,[],[])
    pmin = get_pret(vanzari_ordonate[0])
    assert len(vanzari) == len(vanzari_ordonate)
    for vanzare in vanzari_ordonate:
        assert get_pret(vanzare) >= pmin
        pmin=get_pret(vanzare)



def get_data():
    return [
        creeaza_carte(1, 'b1','g1', 30.0, 'gold'),
        creeaza_carte(2, 'b2', 'g2', 40, 'gold'),
        creeaza_carte(3,'b3','g3',50,'silver'),
        creeaza_carte(4,'b4','g4',60,'gold'),
        creeaza_carte(5,'b5','g5',100,'gold'),
        creeaza_carte(6,'b6','g6',200,'none'),



    ]

