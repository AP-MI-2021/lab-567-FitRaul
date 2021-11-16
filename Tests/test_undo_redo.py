from Logic.crud import create
from Userinterface.console import handle_undo, handle_redo


def test_undo_redo():
    carti=[]
    undo_list=[]
    redo_list=[]
    carti = create(carti, 1, 'Harap Alb', 'Basm', 15, 'gold', undo_list, redo_list)
    assert len(carti) == 1
    carti = create(carti, 2, 'Moara cu noroc', 'Nuvela', 25, 'none', undo_list, redo_list)
    assert len(carti) == 2
    carti = create(carti, 3, 'Mara', 'Roman', 35, 'gold', undo_list, redo_list)
    assert len(carti) == 3
    carti = handle_undo(carti, undo_list, redo_list)
    assert len(carti) == 2
    carti = handle_undo(carti, undo_list, redo_list)
    assert len(carti) == 1
    carti = handle_undo(carti, undo_list, redo_list)
    assert len(carti) == 0
    carti = handle_undo(carti, undo_list, redo_list)
    assert len(carti) == 0
    carti = create(carti, 1, 'Harap Alb', 'Basm', 15, 'gold', undo_list, redo_list)
    carti = create(carti, 2, 'Moara cu noroc', 'Nuvela', 25, 'none', undo_list, redo_list)
    carti = create(carti, 3, 'Mara', 'Roman', 35, 'gold', undo_list, redo_list)
    assert len(carti) == 3
    carti = handle_redo(carti, undo_list, redo_list)
    assert len(carti) == 3
    carti = handle_undo(carti, undo_list, redo_list)
    assert len(carti) == 2
    carti = handle_undo(carti, undo_list, redo_list)
    assert len(carti) == 1
    carti = create(carti, 4, 'Enigma Otiliei', 'Roman', 12, 'silver', undo_list, redo_list)
    assert len(carti) == 2
    carti = handle_redo(carti, undo_list, redo_list)
    assert len(carti) == 2
    carti = handle_undo(carti, undo_list, redo_list)
    assert len(carti) == 1
    carti = handle_undo(carti, undo_list, redo_list)
    assert len(carti) == 0
    carti = handle_redo(carti, undo_list, redo_list)
    assert len(carti) == 1
    carti = handle_redo(carti, undo_list, redo_list)
    assert len(carti) == 2
    carti = handle_redo(carti, undo_list, redo_list)
    assert len(carti) == 2