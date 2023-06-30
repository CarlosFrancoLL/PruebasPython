import pytest
import random
from numerosAmigos import numeros_amigos

numero_random1 = random.randint(220, 1000000)
numero_random2 = random.randint(220, 1000000)

def test_numeros_amigos_1():
    assert numeros_amigos(1184,1210) == "1184 y 1210 son amigos"
    print("La función numeros_amigos_1 funciona correctamente")
    
def test_numeros_amigos_2():
    assert numeros_amigos(1184,1210) == "1184 y 1210 no son amigos"
    print("La función numeros_amigos_2 funciona correctamente")
    
@pytest.mark.parametrize(
    "input_x, input_y, esperado",
    [
        (1500, 2000, "1500 y 2000 no son amigos")
        (10744, 10856, "10744 y 10856 son amigos")
        (numero_random1,numero_random2, "{numero_random1} y {número_random2} son amigos")
        (numero_random1,numero_random2, "{numero_random1} y {número_random2} no son amigos")
    ]
)