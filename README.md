# Projeto Simples em Python

Este é um exemplo básico de aplicação em Python que utiliza as bibliotecas Numpy, Sympy e Pytest para fazer uma calculadora avançada e exibir o resultado.

## Pré-requisitos
- Python 3.10 ou superior
- [Poetry](https://python-poetry.org/docs/)
- Pytest

---

## Rodando o projeto

### Usando **Poetry** 

## 1º passo (Fazer somente na primeira vez)
```bash
poetry install
```

## 2º passo
```bash
poetry run python main.py
```
### Usando **Pytest** 

```bash
pytest testes.py
```



---

# Exercício de testes unitários
Dado que o código e seus testes estavam todos passando.

<img width="1057" height="172" alt="{E2F32549-80CB-49F6-8BCF-DF2DB38CC999}" src="https://github.com/user-attachments/assets/84e4fa11-101c-4f71-8a47-045b6af7c728" />

Durante o exercício o Álvaro criou uma PR com alteração no método 3 de trigonometria da calculadora, que seria equivalente ao método Tangente.

<img width="255" height="162" alt="{19DD8862-9209-49CE-8387-6872B6DAE72B}" src="https://github.com/user-attachments/assets/6fe9445c-2670-439d-9003-e7820dc5df32" />

No teste é verificado se o resultado do cálculo da tangente esperado é o mesmo que o retornado da função de cálculo, logo o teste verificou que tinha um erro no método.

<img width="1050" height="71" alt="{72143B62-5418-46D4-9EE5-BA9583B05269}" src="https://github.com/user-attachments/assets/2011e2e3-c03f-44d0-866e-dd0ed8ef2934" />

Por tanto, foi realizada um PR em que os dados eram corrigidos.

