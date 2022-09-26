class Quadrado:
  def __init__(self, lado):
    self.lado = lado
    
  def area_quadrado(self):
    return self.lado ** 2
  
  def perimetro_quadrado(self):
    return self.lado * 4