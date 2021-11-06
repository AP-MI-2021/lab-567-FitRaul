from Logic.crud import create
from Tests.test_crud import test_crud
from Userinterface.console import run_ui

def main():
    carti = []
    carti = create(carti, 1, 'In Search of Lost Time', 'actiune', 120,'silver')
    carti = create(carti, 2, 'The Woman in White', 'drama', 160, 'none')
    carti = create(carti, 3, 'The Lord of the Rings', 'actiune', 200, 'silver')
    carti = create(carti, 4, 'The Great Gatsby', 'horror', 100, 'none')
    carti = create(carti, 5, 'Uncle Tom Cabin', 'drama', 150, 'gold')
    carti = create(carti, 6, 'Water for Elephants', 'actiune', 110, 'silver')
    carti = run_ui(carti)

if __name__ == '__main__':
    test_crud()
    main()