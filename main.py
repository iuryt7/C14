import sympy as sp
import numpy as np

def calcular_expressao(expr):
    try:
        resultado = sp.sympify(expr)
        return resultado
    except Exception as e:
        return f"Erro na expressão: {e}"

def trigonometria():
    print("Escolha uma operação trigonométrica:")
    print("1. Seno")
    print("2. Cosseno")
    print("3. Tangente")

    escolha = input("Digite a operação desejada (1/2/3): ")

    angulo = float(input("Digite o ângulo (em graus): "))
    angulo_rad = np.radians(angulo)
    if escolha == '1':
        return np.sin(angulo_rad)
    elif escolha == '2':
        return np.cos(angulo_rad)
    elif escolha == '3':
        return np.tan(angulo_rad)
    else:
        return "Opção inválida!"

def derivada(expr):
    x = sp.symbols('x')
    f = sp.sympify(expr)
    return sp.diff(f, x)

def integral(expr):
    x = sp.symbols('x')
    f = sp.sympify(expr)
    return sp.integrate(f, x)

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
        resultado = trigonometria()
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

calculadora_avancada()
