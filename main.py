from Logic.crud import create
from Tests.test_crud import test_crud
from Userinterface.console import run_ui
from Tests.teste import test_reducere_pret,test_modificare_gen,test_titles_count_each_genre,test_sort_ascending
from Tests.test_undo_redo import test_undo_redo


def main():
    carti = []
    undo_list = []
    redo_list = []
    carti = create(carti, 1, 'In Search of Lost Time', 'actiune', 120, 'silver', undo_list, redo_list)
    carti = create(carti, 2, 'The Woman in White', 'drama', 160, 'none', undo_list, redo_list)
    carti = create(carti, 3, 'The Lord of the Rings', 'actiune', 200, 'silver', undo_list, redo_list)
    #carti = create(carti, 4, 'The Great Gatsby', 'horror', 100, 'none', undo_list, redo_list)
    #carti = create(carti, 5, 'Uncle Tom Cabin', 'drama', 150, 'gold', undo_list, redo_list)
    #carti = create(carti, 6, 'Water for Elephants', 'actiune', 110, 'silver', undo_list, redo_list)
    carti = run_ui(carti, undo_list, redo_list)


if __name__ == '__main__':
    test_crud()
    test_reducere_pret()
    test_modificare_gen()
    test_titles_count_each_genre()
    test_sort_ascending()
    test_undo_redo()
    main()