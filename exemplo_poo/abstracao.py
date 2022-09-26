#Empresa de materiais de contrução

from datetime import date

class Product:
  marca = 'XXXX'
  
  def __init__(self, cod, desc, categoria, linha, material):
    self.cod = cod
    self.desc = desc
    self.categoria = categoria
    self.linha = linha
    self.material = material
    self.discount = 0

  def final_date_discount(self):
    self.date_discount = date(2022, 9, 25)
    self.today = date.today()
    self.days = self.date_discount - self.today
    return f'Faltam {self.days.days} dias para a promoção acabar!'

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


if __name__ == "__main__":
  print('\n*************Promoção**************')

  product1 = Metais('Sim', '102030', 'Torneira para Lavatório Bica Alta',
                    'Metais para Banheiro', 'Prisma', 'Metal')
  print(f'Desconto no produto "{product1.cod} - {product1.desc}": {product1.get_discount()}')
  print(product1.final_date_discount())