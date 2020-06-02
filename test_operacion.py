"""
    Desarrollo por Pruebas
    https://docs.pytest.org/en/latest/index.html
"""
from operacion import *
 
def test_suma():
    calc = suma(2, 2)
    assert calc == 4

def test_obtener_suma():
    """
    """
    lista = [1, 2, 3, 4, 10]
    assert 20 == obtener_suma(lista)
