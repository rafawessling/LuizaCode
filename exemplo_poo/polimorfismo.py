#Empresa de materiais de contrução

class Product:
  marca = 'XXXX'
  
  def __init__(self, cod, desc, categoria, linha, material):
    self.cod = cod
    self.desc = desc
    self.categoria = categoria
    self.linha = linha
    self.material = material
    self.discount = 0

  def get_discount(self):
    return self.discount


class Metais(Product):
  def __init__(self, arejador, cod, desc, categoria, linha, material):
    self.arejador = arejador
    super().__init__(cod, desc, categoria, linha, material)
  
  def get_discount(self):
    if self.linha == 'Prisma':
      self.discount = '10%'
    return self.discount
  
  def __str__(self):
    return f'\nCod: {self.cod}\nDescricão: {self.desc}\nArejador: {self.arejador}\n' \
           f'Categoria: {self.categoria}\nLinha: {self.linha}\nMaterial: {self.material}' 
  

class TubulacaoEConexao(Product):
  def __init__(self, diametro, cod, desc, categoria, linha, material):
    self.diametro = diametro
    
    super().__init__(cod, desc, categoria, linha, material)

  def get_discount(self):
    if self.linha == 'Soldável Água Fria':
      self.discount = '15%'
    return self.discount
  
  def __str__(self):
    return f'\nCod: {self.cod}\nDescricão: {self.desc}\nDiâmetro: {self.diametro}\n' \
           f'Categoria: {self.categoria}\nLinha: {self.linha}\nMaterial: {self.material}' 


class CaixaDAgua(Product):
  def __init__(self, capacidade, cod, desc, categoria, linha, material):
    self.capacidade = capacidade
    super().__init__(cod, desc, categoria, linha, material)
  
  def get_discount(self):
    if self.linha == 'Caixas D\'Água':
      self.discount = '7%'
    return self.discount
  
  def __str__(self):
    return f'\nCod: {self.cod}\nDescricão: {self.desc}\nCapacidade: {self.capacidade}\n' \
           f'Categoria: {self.categoria}\nLinha: {self.linha}\nMaterial: {self.material}' 


if __name__ == "__main__":
  print('\n*************Desconto**************')

  product1 = Metais('Sim', '102030', 'Torneira para Lavatório Bica Alta',
                    'Metais para Banheiro', 'Prisma', 'Metal')
  print(f'Desconto no produto "{product1.cod} - {product1.desc}": {product1.get_discount()}')

  product2 = TubulacaoEConexao('25 mm', '111213', 'Tubo Soldável 3m', 
                             'Predial', 'Soldável Água Fria', 'PVC')
  print(f'Desconto no produto "{product2.cod} - {product2.desc}": {product2.get_discount()}')

  product3 = CaixaDAgua('1000L', '100200', 'Caixa D\'Água', 'Predial', 
                       'Caixas D\'Água', 'Polietileno')
  print(f'Desconto no produto "{product3.cod} - {product3.desc}": {product3.get_discount()}')