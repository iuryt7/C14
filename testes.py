import pytest
from main import calcular_expressao, trigonometria, derivada, integral
import sympy as sp
import numpy as np

@pytest.mark.suite1
def test_calcular_expressao():
    assert calcular_expressao('2 + 3') == 5

@pytest.mark.suite1
def test_calcular_expressao_alg():
    x = sp.symbols('x')
    assert calcular_expressao('x + 3') == x + 3

@pytest.mark.suite1
def test_trigonometria_seno():
    assert trigonometria('1', 30) == np.sin(np.radians(30))

@pytest.mark.suite1
def test_trigonometria_cosseno():
    assert trigonometria('2', 60) == np.cos(np.radians(60))

@pytest.mark.suite1
def test_trigonometria_tangente():
    assert trigonometria('3', 45) == np.tan(np.radians(45))

@pytest.mark.suite1
def test_derivada():
    x = sp.symbols('x')
    assert derivada('x**2 + 3*x + 5') == 2*x + 3

@pytest.mark.suite1
def test_integral():
    x = sp.symbols('x')
    assert integral('x**2 + 3*x + 5') == x**3/3 + 3*x**2/2 + 5*x

@pytest.mark.suite1
def test_calcular_expressao_trig():
    x = sp.symbols('x')
    assert calcular_expressao('sin(x) + cos(x)') == sp.sin(x) + sp.cos(x)

@pytest.mark.suite1
def test_calcular_expressao_numero():
    assert calcular_expressao('4 + 5') == 9

@pytest.mark.suite1
def test_calcular_expressao_variaveis():
    x = sp.symbols('x')
    assert calcular_expressao('x + 5') == x + 5

# ===================================================================================================================================

@pytest.mark.suite2
def test_calcular_expressao_invalida():
    assert calcular_expressao('2 + ') == "Erro na expressão: Sympify of expression 'could not parse '2 + '' failed, because of exception being raised:\nSyntaxError: invalid syntax (<string>, line 1)"

@pytest.mark.suite2
def test_trigonometria_opcao_invalida():
    assert trigonometria('5', 30) == "Opção inválida!"

@pytest.mark.suite2
def test_derivada_invalida():
    assert derivada('x**2 + 3x + 5') == "Erro na expressão: Sympify of expression 'could not parse 'x**2 + 3x + 5'' failed, because of exception being raised:\nSyntaxError: invalid syntax (<string>, line 1)"

@pytest.mark.suite2
def test_integral_invalida():
    assert derivada('x**2 + 3x') == "Erro na expressão: Sympify of expression 'could not parse 'x**2 + 3x'' failed, because of exception being raised:\nSyntaxError: invalid syntax (<string>, line 1)"

@pytest.mark.suite2
def test_calcular_expressao_nao_reconhecida():
    assert calcular_expressao('2 * 3 & 5') == "Erro na expressão: operador '&' não permitido."

@pytest.mark.suite2
def test_trigonometria_angulo_invalido():
    assert trigonometria('1', 'invalid') == "Valor de ângulo inválido!"

@pytest.mark.suite2
def test_calcular_expressao_invalida_sqrt():
    assert calcular_expressao('sqrt(-1)') == sp.I

@pytest.mark.suite2
def test_derivada_variavel_nao_definida():
    assert derivada('L**2 + 5') == 'Erro na expressão: SympifyError: "A expressão deve conter apenas a variável \'x\'."'
    
@pytest.mark.suite2
def test_integral_simbolo_errado():
    assert derivada('x*2 + 5t') == "Erro na expressão: Sympify of expression 'could not parse 'x*2 + 5t'' failed, because of exception being raised:\nSyntaxError: invalid syntax (<string>, line 1)"

@pytest.mark.suite2
def test_calcular_expressao_texto():
    assert calcular_expressao('texto aleatório') == "Erro na expressão: Sympify of expression 'could not parse 'texto aleatório'' failed, because of exception being raised:\nSyntaxError: invalid syntax (<string>, line 1)"
