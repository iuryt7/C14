import sympy as sp
import numpy as np

import sympy as sp

def calcular_expressao(expr):

    for operador in ['&', '|', '%', '<<', '>>']:
        if operador in expr:
            return f"Erro na expressão: operador '{operador}' não permitido."

    try:
        resultado = sp.sympify(expr)
        return resultado
    except Exception as e:
        return f"Erro na expressão: {e}"


def trigonometria(escolha, angulo):
    try:
        angulo = float(angulo)
        angulo_rad = np.radians(angulo)
    except ValueError:
        return "Valor de ângulo inválido!"
    if escolha == '1':
        return np.sin(angulo_rad)
    elif escolha == '2':
        return np.cos(angulo_rad)
    elif escolha == '3':
        return np.sin(angulo_rad)
    else:
        return "Opção inválida!"

def derivada(expr):
    x = sp.symbols('x')
    try:
        f = sp.sympify(expr)
        if not all(v == x for v in f.free_symbols):
            raise sp.SympifyError("A expressão deve conter apenas a variável 'x'.")
        
        return sp.diff(f, x)
    except sp.SympifyError as e:
        return f"Erro na expressão: {e}"

def integral(expr):
    x = sp.symbols('x')
    try:
        f = sp.sympify(expr)
        if not all(v == x for v in f.free_symbols):
            raise sp.SympifyError("A expressão deve conter apenas a variável 'x'.")
        
        return sp.integrate(f, x)
    except sp.SympifyError as e:
        return f"Erro na expressão: {e}"

def calculadora_avancada():
    print("Calculadora Avançada - Opções:")
    print("1. Cálculo de expressão matemática (simples ou algébrica)")
    print("2. Funções trigonométricas (seno, cosseno, tangente)")
    print("3. Derivada de uma função")
    print("4. Integral de uma função")

    escolha = input("Escolha a operação (1/2/3/4): ")

    if escolha == '1':
        expr = input("Digite a expressão matemática (ex: 2*x + 3, sin(x) + cos(x)): ")
        resultado = calcular_expressao(expr)
        print(f"Resultado: {resultado}")
    
    elif escolha == '2':
        resultado = trigonometria(input("Escolha a operação trigonométrica (1-seno, 2-cosseno, 3-tangente): "), 
                                  float(input("Digite o ângulo (em graus): ")))
        print(f"Resultado trigonométrico: {resultado}")

    elif escolha == '3':
        expr = input("Digite a função para derivada (ex: x**2 + 3*x + 5): ")
        resultado = derivada(expr)
        print(f"Derivada: {resultado}")
    
    elif escolha == '4':
        expr = input("Digite a função para integral (ex: x**2 + 3*x + 5): ")
        resultado = integral(expr)
        print(f"Integral: {resultado}")
    
    else:
        print("Opção inválida!")

if __name__ == "__main__":
    calculadora_avancada()
