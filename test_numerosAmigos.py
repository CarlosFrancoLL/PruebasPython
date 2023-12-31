"""Se realizaron las pruebas con intención de que fallaran 5
de las pruebas, se usaron el mismo número con grupos de 2 pruebas
y por determinar debían de fallar en una u otra ya que es imposible
que la función de ambos resultados. Los únicos con números diferentes
son la 9 y la 10. Eso dejaría que los test_numeros_amigos 2, 4, 5, 7, 9
fallen la prueba (5/10) y los demás la superen (5/10).
"""
import pytest
from numerosAmigos import numeros_amigos

def test_numeros_amigos_1():
    assert numeros_amigos(1184,1210) == "1184 y 1210 son amigos"
    print("La función numeros_amigos_1 funciona correctamente")
    
def test_numeros_amigos_2():
    assert numeros_amigos(1184,1210) == "1184 y 1210 no son amigos"
    print("La función numeros_amigos_2 funciona correctamente")
    
def test_numeros_amigos_3():
    assert numeros_amigos(2620, 2924) == "2620 y 2924 son amigos"
    print("La función numeros_amigos_3 funciona correctamente")
    
def test_numeros_amigos_4():
    assert numeros_amigos(2620, 2924) == "2620 y 2924 no son amigos"
    print("La función numeros_amigos_4 funciona correctamente")
    
def test_numeros_amigos_5():
    assert numeros_amigos(1000, 2000) == "1000 y 2000 son amigos"
    print("La función numeros_amigos_5 funciona correctamente")
    
def test_numeros_amigos_6():
    assert numeros_amigos(1000, 2000) == "1000 y 2000 no son amigos"
    print("La función numeros_amigos_6 funciona correctamente")
    
def test_numeros_amigos_7():
    assert numeros_amigos(85848, 22951) == "85848 y 22951 son amigos"
    print("La función numeros_amigos_7 funciona correctamente")
    
def test_numeros_amigos_8():
    assert numeros_amigos(85848, 22951) == "85848 y 22951 no son amigos"
    print("La función numeros_amigos_8 funciona correctamente")
    
def test_numeros_amigos_9():
    assert numeros_amigos(66928, 66992) == "66928 y 66992 no son amigos"
    print("La función numeros_amigos_9 funciona correctamente")

def test_numeros_amigos_10():
    assert numeros_amigos(29966, 82966) == "29966 y 82966 no son amigos"
    print("La función numeros_amigos_10 funciona correctamente")