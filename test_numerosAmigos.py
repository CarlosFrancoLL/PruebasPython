from numerosAmigos import numeros_amigos

def test_numeros_amigos_1():
    assert numeros_amigos(1184,1210) == "1184 y 1210 son amigos"
    
def test_numeros_amigos_2():
    assert numeros_amigos(1184,1210) == "1184 y 1210 no son amigos"
    
