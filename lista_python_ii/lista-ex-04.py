#Crie um professor de classe com atributos nome, idade e salário, onde o
#salário deve ter um método privado que não pode ser acessado fora da classe.
#a) Crie um método para acessar o método privado, onde é passada
#a identificação do usuário se ele pode ou não acessar.

class Teacher:
  def __init__(self, name, age, salary):
    self.name = name
    self.age = age
    self.salary = salary
  
  def _get_salary_access(self):
    return f'Salário: R$ {self.salary}.'
  
  def access_salary(self, id_user):
    if id_user == '1010':
      return self._get_salary_access()
    
    return 'Você não tem acesso a essa informacão.'
  
person = Teacher('Maria', '40', '5000')

access = person.access_salary('1010')
print(access)

access = person.access_salary('1020')
print(access)