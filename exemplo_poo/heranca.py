#Empresa de materiais de contrução

class Product:
  marca = 'XXXX'
  
  def __init__(self, cod, desc, categoria, linha, material):
    self.cod = cod
    self.desc = desc
    self.categoria = categoria
    self.linha = linha
    self.material = material


class Metais(Product):
  def __init__(self, arejador, cod, desc, categoria, linha, material):
    self.arejador = arejador
    super().__init__(cod, desc, categoria, linha, material)
  
  def __str__(self):
    return f'Cod: {self.cod}\nDescricão: {self.desc}\nArejador: {self.arejador}\n' \
           f'Categoria: {self.categoria}\nLinha: {self.linha}\nMaterial: {self.material}\n' 


class TubulacaoEConexao(Product):
  def __init__(self, diametro, cod, desc, categoria, linha, material):
    self.diametro = diametro
    
    super().__init__(cod, desc, categoria, linha, material)

  def __str__(self):
    return f'Cod: {self.cod}\nDescricão: {self.desc}\nDiâmetro: {self.diametro}\n' \
           f'Categoria: {self.categoria}\nLinha: {self.linha}\nMaterial: {self.material}\n' 


class CaixaDAgua(Product):
  def __init__(self, capacidade, cod, desc, categoria, linha, material):
    self.capacidade = capacidade
    super().__init__(cod, desc, categoria, linha, material)
  
  def __str__(self):
    return f'Cod: {self.cod}\nDescricão: {self.desc}\nCapacidade: {self.capacidade}\n' \
           f'Categoria: {self.categoria}\nLinha: {self.linha}\nMaterial: {self.material}\n' 


if __name__ == "__main__":
  print('\n*************Produtos**************')

  product1 = Metais('Sim', '102030', 'Torneira para Lavatório Bica Alta',
                    'Metais para Banheiro', 'Prisma', 'Metal')
  print(product1)

  product2 = TubulacaoEConexao('25 mm', '111213', 'Tubo Soldável 3m', 
                             'Predial', 'Soldável Água Fria', 'PVC')
  print(product2)

  product3 = CaixaDAgua('1000L', '100200', 'Caixa D\'Água', 'Predial', 
                       'Caixas D\'Água', 'Polietileno')
  print(product3)