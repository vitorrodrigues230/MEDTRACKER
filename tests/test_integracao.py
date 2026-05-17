import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import buscar_cep

def test_buscar_cep_sucesso_integracao():

    resultado = buscar_cep("70790-075")
    
    assert "erro" not in resultado
    assert resultado["cidade"] == "Brasília"
    assert resultado["uf"] == "DF"

def test_buscar_cep_inexistente_integracao():

    resultado = buscar_cep("99999-999")
    
    assert "erro" in resultado
    assert resultado["erro"] == "CEP não encontrado."