        ##############################################  
        #                                          #
        #                                        #
        #                                      #
        #                                    #
        #                                  #
        #                                #
        #                              #
        #                            #
        #             ###############
        #             #
        #             #
        #             #
        #             # 
        #             # 
        #             # 
        #             #
        ###############


#create vehicle class
class Vehicle:
  #initialize variables (year, model, & make)
  def __init__(self, year, model, make):
    self.year = year
    self.model = model
    self.make = make 

  #create year method
  def year(self):
    return self.year


  #create model method
  def model(self):
    return self.model


  #create make method
  def make(self):
    return self.make


#create mazda class
class Mazda(Vehicle):

  #initialize variables
  def __init__(self, year, model, make, turbo):
    super().__init__(year,model,make)
    self.turbo = turbo


  #create turbo method
  def turbo(self):
    return self.turbo

v1 = Vehicle(2010, "Escape", "Ford")
print(v1.year)
print(v1.make)
print(v1.model)

m1 = Mazda(1999, "Mx-5 Miata", "Mazda", False)
print(m1.year)
print(m1.make)
print(m1.model)
print(m1.turbo)
