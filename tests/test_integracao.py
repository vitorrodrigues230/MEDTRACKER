import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from medtracker import SistemaMedTracker

def test_buscar_cep_sucesso_integracao():
    sistema = SistemaMedTracker()
    
    resultado = sistema.buscar_endereco_por_cep("70790-075")
    
    assert "erro" not in resultado
    assert resultado["cidade"] == "Brasília"
    assert resultado["estado"] == "DF"

def test_buscar_cep_inexistente_integracao():
    
    sistema = SistemaMedTracker()
    resultado = sistema.buscar_endereco_por_cep("99999-999")
    
    assert "erro" in resultado
    assert resultado["erro"] == "CEP não encontrado."