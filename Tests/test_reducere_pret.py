from Domain.carte import creaza_carte, get_pret_carte
from Logic.discount import discount_function


def get_data():
    return [
        creaza_carte(1, 'carte1', 'gen1', 99, 'silver'),
        creaza_carte(2, 'carte2', 'gen2', 40, 'none'),
        creaza_carte(3, 'carte3', 'gen3', 88, 'gold'),
        creaza_carte(4, 'carte4', 'gen4', 32, 'silver'),
    ]

def test_discount():
    carti = get_data()
    new_carti = discount_function(carti)
    assert len(new_carti) == 4
    assert get_pret(new_carti[0]) == 94.05
    assert get_pret(new_carti[1]) == 40
    assert get_pret(new_carti[2]) == 79.2