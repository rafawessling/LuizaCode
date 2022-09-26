#Dada as seguintes informações: Pessoa, cpf, nome e idade, crie uma
#classe onde teremos o retorno do documento, o retorno do nome e
#verificação de tipo de pessoa, onde um método irá receber como
#parâmetro “F” ou “N” para trazer fumante ou não fumante.
#Feito isso, crie uma instância e retorne esses valores

class Person:
  def __init__(self, cpf, name, age, verify_person):
    self.cpf = cpf
    self.name = name
    self.age = age
    self.verify_person = verify_person
  
  def get_cpf(self):
    return f'CPF: {self.cpf}.'
  
  def get_name(self):
    return f'Nome: {self.name}.'
  
  def get_age(self):
    return f'Idade: {self.age}.'
  
  def get_verify_person(self):
    if self.verify_person == 'N':
      return f'Não Fumante.'
    
    return f'Fumanete.'

person = Person('012345678-90', 'Joana', '30', 'N')
print(person.get_cpf())
print(person.get_name())
print(person.get_age())
print(person.get_verify_person())