import math

class GeometriaAnalitica:
    def __init__(self):
        pass

    def distancia(self, ponto1, ponto2):
        """Calcula a distância entre dois pontos."""
        return math.sqrt((ponto2[0] - ponto1[0])**2 + (ponto2[1] - ponto1[1])**2)

    def ponto_medio(self, ponto1, ponto2):
        """Calcula o ponto médio entre dois pontos."""
        return ((ponto1[0] + ponto2[0]) / 2, (ponto1[1] + ponto2[1]) / 2)

    def coeficiente_angular(self, ponto1, ponto2):
        """Calcula o coeficiente angular de uma reta passando por dois pontos."""
        if ponto2[0] - ponto1[0] == 0:
            return float('inf')  # Linha vertical
        return (ponto2[1] - ponto1[1]) / (ponto2[0] - ponto1[0])

    def equacao_reta(self, ponto1, ponto2):
        """Retorna a equação de uma reta na forma y = mx + b."""
        m = self.coeficiente_angular(ponto1, ponto2)
        if m == float('inf'):
            return f"x = {ponto1[0]}"
        b = ponto1[1] - m * ponto1[0]
        return f"y = {m}x + {b}"

    def distancia_ponto_reta(self, ponto, reta_ponto1, reta_ponto2):
        """Calcula a distância de um ponto a uma reta."""
        A = self.coeficiente_angular(reta_ponto1, reta_ponto2)
        B = -1
        C = reta_ponto1[1] - A * reta_ponto1[0]
        return abs(A * ponto[0] + B * ponto[1] + C) / math.sqrt(A**2 + B**2)

    def sao_colineares(self, ponto1, ponto2, ponto3):
        """Verifica se três pontos são colineares."""
        return (ponto2[0] - ponto1[0]) * (ponto3[1] - ponto1[1]) == (ponto3[0] - ponto1[0]) * (ponto2[1] - ponto1[1])

    def equacao_circulo(self, centro, ponto_na_circunferencia):
        """Retorna a equação de um círculo dado seu centro e um ponto na circunferência."""
        raio = self.distancia(centro, ponto_na_circunferencia)
        return f"(x - {centro[0]})^2 + (y - {centro[1]})^2 = {raio**2}"

    def area_circulo(self, centro, ponto_na_circunferencia):
        """Calcula a área de um círculo dado seu centro e um ponto na circunferência."""
        raio = self.distancia(centro, ponto_na_circunferencia)
        return math.pi * raio**2

    def circunferencia_circulo(self, centro, ponto_na_circunferencia):
        """Calcula a circunferência de um círculo dado seu centro e um ponto na circunferência."""
        raio = self.distancia(centro, ponto_na_circunferencia)
        return 2 * math.pi * raio

    def intersecao_retas(self, reta1_ponto1, reta1_ponto2, reta2_ponto1, reta2_ponto2):
        """Encontra o ponto de interseção de duas retas."""
        x1, y1 = reta1_ponto1
        x2, y2 = reta1_ponto2
        x3, y3 = reta2_ponto1
        x4, y4 = reta2_ponto2

        det = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        if det == 0:
            return None  # Retas são paralelas

        px = ((x1*y2 - y1*x2) * (x3 - x4) - (x1 - x2) * (x3*y4 - y3*x4)) / det
        py = ((x1*y2 - y1*x2) * (y3 - y4) - (y1 - y2) * (x3*y4 - y3*x4)) / det

        return (px, py)

    def angulo_entre_retas(self, reta1_ponto1, reta1_ponto2, reta2_ponto1, reta2_ponto2):
        """Calcula o ângulo entre duas retas."""
        m1 = self.coeficiente_angular(reta1_ponto1, reta1_ponto2)
        m2 = self.coeficiente_angular(reta2_ponto1, reta2_ponto2)
        
        if m1 == float('inf') and m2 == float('inf'):
            return 0  # Retas verticais paralelas
        elif m1 == float('inf') or m2 == float('inf'):
            return math.pi / 2  # Retas perpendiculares
        
        tan_theta = abs((m2 - m1) / (1 + m1 * m2))
        return math.atan(tan_theta)

# Exemplo de uso
geo = GeometriaAnalitica()

# Calcular distância entre dois pontos
print(f"Distância entre (0, 0) e (3, 4): {geo.distancia((0, 0), (3, 4))}")

# Encontrar ponto médio
print(f"Ponto médio entre (0, 0) e (6, 8): {geo.ponto_medio((0, 0), (6, 8))}")

# Calcular coeficiente angular
print(f"Coeficiente angular da reta passando por (0, 0) e (3, 4): {geo.coeficiente_angular((0, 0), (3, 4))}")

# Obter equação da reta
print(f"Equação da reta passando por (0, 0) e (3, 4): {geo.equacao_reta((0, 0), (3, 4))}")

# Calcular distância de um ponto a uma reta
print(f"Distância do ponto (0, 5) à reta passando por (0, 0) e (3, 4): {geo.distancia_ponto_reta((0, 5), (0, 0), (3, 4))}")

# Verificar se pontos são colineares
print(f"Os pontos (0, 0), (1, 1) e (2, 2) são colineares? {geo.sao_colineares((0, 0), (1, 1), (2, 2))}")

# Obter equação do círculo
print(f"Equação do círculo com centro (0, 0) passando por (3, 4): {geo.equacao_circulo((0, 0), (3, 4))}")

# Calcular área do círculo
print(f"Área do círculo com centro (0, 0) passando por (3, 4): {geo.area_circulo((0, 0), (3, 4))}")

# Calcular circunferência do círculo
print(f"Circunferência do círculo com centro (0, 0) passando por (3, 4): {geo.circunferencia_circulo((0, 0), (3, 4))}")

# Encontrar interseção de duas retas
print(f"Interseção das retas (0, 0)-(3, 4) e (0, 5)-(5, 0): {geo.intersecao_retas((0, 0), (3, 4), (0, 5), (5, 0))}")

# Calcular ângulo entre duas retas
print(f"Ângulo entre as retas (0, 0)-(3, 4) e (0, 5)-(5, 0): {geo.angulo_entre_retas((0, 0), (3, 4), (0, 5), (5, 0))}")