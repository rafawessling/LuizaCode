#Escreva uma classe “PessoaFisica” e herde Pessoa, crie um método
#exclusivo para a classe e acesse-o

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
    
    return f'Fumante.'

class NaturalPerson(Person):
  def __init__(self, cpf, name, age, verify_person, type_person):
    self.type_person = type_person
    
    super().__init__(cpf, name, age, verify_person)
  
  def get_type_person(self):
    if self.type_person == 'PF':
      return f'Pessoa Física.'
    
    return f'Pessoa Jurídica.'

person = NaturalPerson('012345678-90', 'Joana', '30', 'N', 'PF')
print(person.get_cpf())
print(person.get_name())
print(person.get_age())
print(person.get_verify_person())
print(person.get_type_person())