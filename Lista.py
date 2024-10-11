import sympy as sp

# Definindo variáveis simbólicas
x, y = sp.symbols('x y')

def distancia_entre_pontos():
    """Solicita dois pontos e calcula a distância entre eles"""
    print("Informe as coordenadas dos dois pontos:")
    x1, y1 = map(float, input("Ponto A (x1 y1): ").split())
    x2, y2 = map(float, input("Ponto B (x2 y2): ").split())
    
    distancia = sp.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    print(f"Distância entre A e B: {distancia}")

def equacao_da_reta():
    """Solicita dois pontos e encontra a equação da reta que passa por eles"""
    print("Informe as coordenadas dos dois pontos:")
    x1, y1 = map(float, input("Ponto A (x1 y1): ").split())
    x2, y2 = map(float, input("Ponto B (x2 y2): ").split())
    
    # Verifica se a reta é vertical
    if x1 == x2:
        print(f"A reta é vertical: x = {x1}")
    else:
        # Inclinação da reta (m) e equação na forma y = mx + c
        m = (y2 - y1) / (x2 - x1)
        c = y1 - m * x1
        equacao = sp.Eq(y, m * x + c)
        print(f"Equação da reta: {equacao}")

def ponto_medio():
    """Solicita dois pontos e calcula o ponto médio"""
    print("Informe as coordenadas dos dois pontos:")
    x1, y1 = map(float, input("Ponto A (x1 y1): ").split())
    x2, y2 = map(float, input("Ponto B (x2 y2): ").split())
    
    ponto_medio = ((x1 + x2) / 2, (y1 + y2) / 2)
    print(f"Ponto médio entre A e B: {ponto_medio}")

def equacao_da_circunferencia():
    """Solicita o centro e o raio e calcula a equação da circunferência"""
    print("Informe o centro e o raio da circunferência:")
    cx, cy = map(float, input("Centro (cx cy): ").split())
    raio = float(input("Raio: "))
    
    equacao = sp.Eq((x - cx)**2 + (y - cy)**2, raio**2)
    print(f"Equação da circunferência: {equacao}")

def menu():
    """Menu principal para selecionar a operação"""
    print("Escolha uma operação de Geometria Analítica:")
    print("1 - Distância entre dois pontos")
    print("2 - Equação da reta que passa por dois pontos")
    print("3 - Ponto médio entre dois pontos")
    print("4 - Equação da circunferência")
    
    opcao = input("Digite o número da operação desejada: ")
    
    if opcao == "1":
        distancia_entre_pontos()
    elif opcao == "2":
        equacao_da_reta()
    elif opcao == "3":
        ponto_medio()
    elif opcao == "4":
        equacao_da_circunferencia()
    else:
        print("Opção inválida. Tente novamente.")

# Executar o menu
menu()
