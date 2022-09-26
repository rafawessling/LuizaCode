#Escreva uma classe “PessoaJurica” e herde Pessoa, agora
#modificando o comportamento, retorne o cnpj. Crie uma instância e
#acesse os dados

class Person:
  def __init__(self, name, age, verify_person, type_person):
    self.name = name
    self.age = age
    self.verify_person = verify_person
    self.type_person = type_person
  
  def get_name(self):
    return f'Name: {self.name}.'
  
  def get_age(self):
    return f'Idade: {self.age}.'
  
  def get_verify_person(self):
    if self.verify_person == 'N':
      return f'Não Fumante'
    return f'Fumante.'
  
  def get_type_person(self):
    if self.type_person == 'PF':
      return f'Pessoa Física.'
    
    return f'Pessoa Jurídica.'

class NaturalPerson(Person):
  def __init__(self, cpf, name, age, verify_person, type_person):
    self.cpf = cpf
    
    super().__init__(name, age, verify_person, type_person)
  
  def get_cpf(self):
    return f'CPF: {self.cpf}.'
  
class LegalEntity(Person):
  def __init__(self, cnpj, name, age, verify_person, type_person):
    self.cnpj = cnpj

    super().__init__(name, age, verify_person, type_person)
    
  def get_cnpj(self):
    return f'CNPJ: {self.cnpj}'


person = NaturalPerson('012345678-90', 'João', '25', 'N', 'PF')
print(person.get_cpf())
print(person.get_name())
print(person.get_age())
print(person.get_verify_person())
print(person.get_type_person())

person = LegalEntity('12.345.678/0001-90', 'Joana', '30', 'S', 'PJ')
print(f'\n{person.get_cnpj()}')
print(person.get_name())
print(person.get_age())
print(person.get_verify_person())
print(person.get_type_person())