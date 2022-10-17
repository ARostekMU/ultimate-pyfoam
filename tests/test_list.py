from ultimate_pyfoam.list import OfList

def test_list_can_be_created():
    a = OfList('name', [1, 2, 3])

def test_format_list():
    a = OfList('name', [1, 2, 3])
    b = '''name (
    1
    2
    3
    ); '''