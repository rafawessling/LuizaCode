#Empresa de materiais de contrução

class Product:
  marca = 'XXXX'
  
  def __init__(self, cod, desc, categoria, linha, material):
    self.cod = cod
    self.desc = desc
    self.categoria = categoria
    self.linha = linha
    self.material = material
    self.receita = 0
    self.senha = '123456'
  
  def _get_receita(self):
    if self.cod == '102030':
      self.receita = 200856.00
    elif self.cod == '111213':
      self.receita = 1002345.00
    elif self.cod == '100200':
      self.receita = 550363.00
    
    return self.receita
      
  def access_receita(self, senha):
    if senha == self.senha:
      return self._get_receita()
    
    print(f'Você não possui acesso à essa informacão\n')
    return None


class Metais(Product):
  def __init__(self, arejador, cod, desc, categoria, linha, material):
    self.arejador = arejador
    super().__init__(cod, desc, categoria, linha, material)
  
  def __str__(self):
    return f'Cod: {self.cod}\nDescricão: {self.desc}\nArejador: {self.arejador}\n' \
           f'Categoria: {self.categoria}\nLinha: {self.linha}\nMaterial: {self.material}' 


class TubulacaoEConexao(Product):
  def __init__(self, diametro, cod, desc, categoria, linha, material):
    self.diametro = diametro
    
    super().__init__(cod, desc, categoria, linha, material)

  def __str__(self):
    return f'Cod: {self.cod}\nDescricão: {self.desc}\nDiâmetro: {self.diametro}\n' \
           f'Categoria: {self.categoria}\nLinha: {self.linha}\nMaterial: {self.material}' 


class CaixaDAgua(Product):
  def __init__(self, capacidade, cod, desc, categoria, linha, material):
    self.capacidade = capacidade
    super().__init__(cod, desc, categoria, linha, material)
  
  def __str__(self):
    return f'Cod: {self.cod}\nDescricão: {self.desc}\nCapacidade: {self.capacidade}\n' \
           f'Categoria: {self.categoria}\nLinha: {self.linha}\nMaterial: {self.material}' 


if __name__ == "__main__":
  print('\n*************Receita**************')

  product1 = Metais('Sim', '102030', 'Torneira para Lavatório Bica Alta',
                    'Metais para Banheiro', 'Prisma', 'Metal')

  receita1 = product1.access_receita('123456')
  if receita1:
    print(f'Receita do produto "{product1.cod} - {product1.desc}" em 2021: R$ {product1.receita}\n')

  product2 = TubulacaoEConexao('25 mm', '111213', 'Tubo Soldável 3m', 
                              'Predial', 'Soldável Água Fria', 'PVC')
  
  receita2 = product2.access_receita('123456')
  if receita2:
    print(f'Receita do produto "{product2.cod} - {product2.desc}" em 2021: R$ {product2.receita}\n')

  product3 = CaixaDAgua('1000L', '100500', 'Caixa D\'Água', 'Predial', 
                        'Caixas D\'Água', 'Polietileno')
  
  receita3 = product3.access_receita('123455')
  if receita3:
    print(f'Receita do produto "{product3.cod} - {product3.desc}" em 2021: R$ {product3.receita}\n')