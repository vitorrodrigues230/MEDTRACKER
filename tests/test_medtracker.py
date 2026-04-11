import sys
import os

# Adiciona a raiz do projeto ao path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Agora o import é direto, sem o 'src.'
from medtracker import SistemaMedTracker

def test_adicionar_medicamento_sucesso():
    sistema = SistemaMedTracker()
    resultado = sistema.adicionar_medicamento("Dipirona", "08:00")
    assert "adicionado com sucesso" in resultado
    assert len(sistema.medicamentos) == 1

def test_adicionar_medicamento_invalido():
    sistema = SistemaMedTracker()
    resultado = sistema.adicionar_medicamento("", "08:00")
    assert "Erro" in resultado
    assert len(sistema.medicamentos) == 0

def test_listar_sistema_vazio():
    sistema = SistemaMedTracker()
    resultado = sistema.listar_medicamentos()
    assert resultado == "Nenhum medicamento cadastrado."