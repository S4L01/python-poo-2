import pytest
from banco.models.conta import conta

@pytest.fixture
def conta_valida():
    return conta(10,11)

def test_atributo_numero_conta(conta_valida):
    assert conta_valida.numero_conta == 10

    
def test_atributo_saldo(conta_valida):
    assert conta_valida.saldo == 0

def test_atributo_depositar_positivo(conta_valida):
    conta_valida.depositar(100)
    assert conta_valida.saldo == 100
