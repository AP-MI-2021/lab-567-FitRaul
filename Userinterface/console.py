from Domain.carte import get_str, get_titlu, get_pret, get_gen, get_tip_reducere, \
    creeaza_carte
from Logic.crud import create, read, update, delete
from Logic.reducere_pret import reducere_pret_pentru_nume
from Logic.min_pret_per_gen import get_min_pret_per_gen
from Logic.modify_title_by_gen import modify_gen_by_title
from Logic.undo_redo import do_undo, do_redo



def show_menu():
    print('1. CRUD')
    print('2. Reducere pret pentru anumite carti.')
    print('3. Modificarea genului pentru un titlu dat ')
    print('4. Cartile cu pret minim din fiecare gen.')
    print('5. Ordonarea cartilor crescator dupa pret')
    print('6. Afisarea numarului de titluri distincte din fiecare an')
    print('u. Undo ')
    print('r. Redo ')
    print('x. Exit')


def handle_add(carti, undo_list, redo_list):
    try:
        id_carte = int(input('Dati id-ul cartii: '))
        titlu = input('Dati titlul cartii: ')
        gen = (input('Dati genul cartii: '))
        pret = float(input('Dati pretul cartii: '))
        tip_reducere = input('Dati tipul de reducere al cartii: ')
        return create(carti, id_carte, titlu, gen, pret, tip_reducere, undo_list, redo_list)
    except ValueError as ve:
        print('Eroare:',ve)

    return carti


def handle_show_all(carti):
    for carte in carti:
        print(get_str(carte))


def handle_show_details(carti):
    id_carte = int(input('Dati id-ul cartii pentru care doriti detalii: '))
    carte = read(carti, id_carte)
    print(f'Titlu: {get_titlu(carte)}')
    print(f'Pret: {get_pret(carte)}')
    print(f'gen: {get_gen(carte)}')
    print(f'tip reducere: {get_tip_reducere(carte)}')


def handle_update(carti, undo_list, redo_list):
    try:
        id_carte = int(input('Dati id-ul cartii care se actualizeaza: '))
        titlu = input('Dati noul titlu al cartii: ')
        pret = float(input('Dati noul pret al cartii: '))
        gen = int(input('Dati noile genuri ale cartii: '))
        tip_reducere = input('Dati noul tip de reducere al cartii: ')
        updated=creeaza_carte(id_carte, titlu, pret, gen, tip_reducere)
        return update(carti, updated,  undo_list, redo_list)
    except ValueError as ve:
        print('Eroare', ve)

    return carti


def handle_delete(carti, undo_list, redo_list):
    try:
        id_carte = int(input('Dati id-ul cartii care se va sterge: '))
        carti= delete(carti, id_carte, undo_list, redo_list)
        print('Stergerea a fost efectuata cu succes.')
        return carti
    except ValueError as ve:
        print('Eroare', ve)

    return carti


def handle_crud(carti, undo_list, redo_list):
    while True:
        print('1. Adaugare')
        print('2. Modificare')
        print('3. Stergere')
        print('a. Afisare')
        print('d. Detalii carte')
        print('b. Revenire')

        optiune = input('Optiunea aleasa: ')
        if optiune == '1':
            carti = handle_add(carti, undo_list, redo_list)
        elif optiune == '2':
            carti = handle_update(carti, undo_list, redo_list)
        elif optiune == '3':
            carti = handle_delete(carti, undo_list, redo_list)
        elif optiune == 'a':
            handle_show_all(carti)
        elif optiune == 'd':
            handle_show_details(carti)
        elif optiune == 'b':
            break
        else:
            print('Optiune invalida.')
    return carti


def handle_reducere_pret(carti, undo_list, redo_list):
    try:
        nume=input('Dati stringul cautat in nume pentru reducerea preturilor: ')
        procentaj=float(input('Dati procentajul cu care va fi redus pretul (intre 0 si 100):'))

        carti=reducere_pret_pentru_nume(carti, nume, procentaj, undo_list, redo_list)

        print('Preturile au fost reduse cu succes.')
    except ValueError as ve:
        print('Eroare', ve)

    return carti


def handle_min_pret_per_gen(carti):
    result = get_min_pret_per_gen(carti)

    for gen in result:
        print(f'{gen}: {get_str(result[gen])}')


def handle_modify_gen_by_title(carti, undo_list, redo_list):
    try:
        titlu=input('Dati titlul cautat pentru schimbarea genului: ')

        carti=modify_gen_by_title(carti, titlu, undo_list, redo_list)

        print('Genul a fost schimbat cu succes.')
    except ValueError as ve:
        print('Eroare', ve)

    return carti


def handle_undo(carti, undo_list, redo_list):
    undo_result = do_undo(undo_list, redo_list, carti)
    if undo_result is not None:
        return undo_result
    return carti


def handle_redo(carti, undo_list, redo_list):
    redo_result = do_redo(undo_list, redo_list, carti)
    if redo_result is not None:
        return redo_result
    return carti


def run_ui(carti, undo_list, redo_list):

    while True:
        handle_show_all(carti)
        show_menu()
        optiune = input('Optiunea aleasa: ')
        if optiune == '1':
            carti = handle_crud(carti, undo_list, redo_list)
        elif optiune == '2':
            carti = handle_reducere_pret(carti, undo_list, redo_list)
        elif optiune == '3':
            carti= handle_modify_gen_by_title(carti, undo_list, redo_list)
        elif optiune== '4':
            handle_min_pret_per_gen(carti)
        elif optiune == 'u':
            carti = handle_undo(carti, undo_list, redo_list)
        elif optiune == 'r':
            carti = handle_redo(carti, undo_list, redo_list)
        elif optiune == 'x':
            break
        else:
            print('Optiune invalida.')

    return carti