#create employee class
class Employee:
  #initialize variables(name,age,income,employeeid)
  def __init__(self, name, age, income, employee_id):
    self.name = name
    self.age = age
    self.income = income
    self.employee_id = employee_id

  #create name method
  @property
  def name(self):
    return self.name

  #create age method
  @property
  def age(self):
    return self.age

  #create income method
  def income(self):
    return self.income

  #create eemployeeid method
  def ID(self):
    return self.employee_id

  #create name / age setter
  @name.setter
  def name(self, new_name):
    self.name = new_name
    return new_name
  
  @age.setter
  def age(self,new_age):
    self.age = new_age
    return new_age

#create developer class
class Developer(Employee):
  #initialize all variables
  def __init__(self, name, age, income, employee_id, language):
    super().__init__(name,age,income,employee_id)
    self.language = language

  #create language method
  def language(self):
    return self.language

  #create language setter
  @language.setter
  def language(self, new_language):
    self.language = new_language
  
