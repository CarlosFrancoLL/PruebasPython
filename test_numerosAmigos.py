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