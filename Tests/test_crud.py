from Domain.carte import creeaza_carte, get_id
from Logic.crud import create, read, update, delete


def get_data():
    return [
        creeaza_carte(1,  'titlu 1', 'horror', 50, 'silver'),
        creeaza_carte(2,  'titlu 2', 'sci-fi', 80.32, 'gold'),
        creeaza_carte(3,  'titlu 3', 'actiune',130, 'silver'),
        creeaza_carte(4,  'titlu 4', 'drama', 150, 'none'),
        creeaza_carte(5,  'titlu 5', 'horror', 40.32, 'gold'),
   ]


def test_create():
    carti = get_data()
    params = (100, 'cnew', 'gen new', 130, 'reducere new')
    p_new = creeaza_carte(*params)
    new_carti = create(carti, *params)
    assert len(new_carti) == len(carti) + 1
    assert p_new in new_carti
    #Testam daca se lanseaza exceptie pentru id duplicat
    params2=(1, 'gdsgwg', 'gewgdsg', 120,'silver')
    try:
        _ =create(new_carti, *params2)
        assert False
    except ValueError:
        assert True


def test_read():
    carti = get_data()
    some_p = carti[2]
    assert read(carti, get_id(some_p)) == some_p
    assert read(carti, None) == carti


def test_update():
    carti = get_data()
    p_updated = creeaza_carte(1, 'new name', 'new gen', 111, 'new reducere')
    updated = update(carti, p_updated)
    assert p_updated in updated
    assert p_updated not in carti
    assert len(updated) == len(carti)


def test_delete():
    carti = get_data()
    to_delete = 3
    p_deleted = read(carti, to_delete)
    deleted = delete(carti, to_delete)
    assert p_deleted not in deleted
    assert p_deleted in carti
    assert len(deleted) == len(carti) - 1


def test_crud():
    test_create()
    test_read()
    test_update()
    test_delete()