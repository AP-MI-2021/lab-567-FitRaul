from Domain.carte import get_str
from Logic.crud import create, delete


def show_menu_in_line():
    print('Cartile se adauga folosind comanda add, id, nume, gen, pret, tip_reducere')
    print('Cartile se afiseaza folosind comanda showall')
    print('Puteti sterge carti din lista de carti folosind comanda "delete" si introducand un id al unei carti existente')
    print('Toate comenzile trebuie apelate pe o singura linie si separate prin ", ".')
    print('')


def command_line_console(carti, undo_list, redo_list):
    """
    Noua consola.
    :param carti:lista de carti
    :param undo_list:
    :param redo_list:
    :return:
    """

    command_line_str = input('Introduceti comanda: ')
    command_line = []
    command_line_str_split = command_line_str.split(', ')
    for index in command_line_str_split:
        command_line.append(index)
    for index in range(0, len(command_line)):
        if command_line[index] == 'add':
            try:
                carti = create(carti, int(command_line[index + 1]), command_line[index + 2],
                             command_line[index + 3], float(command_line[index + 4]), command_line[index + 5], undo_list, redo_list)
            except ValueError as ve:
                print('Eroare! Detalii: ', ve)
        elif command_line[index] == 'showall':
            for carte in carti:
                print(get_str(carte))
        elif command_line[index] == 'delete':
            try:
                carti = delete(carti, int(command_line[index + 1]),undo_list, redo_list)
            except ValueError:
                print( 'Id-ul introdus nu exista, se va trece peste!')
    return carti