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


#create human class
class Human:
  #create language class variable
  language = "English"
  #initialize all variables(name,age,race,weight,speak)
  def __init__(self, name, age, race, weight, speak):
    self.name = name
    self.age = age
    self.race = race
    self.weight = weight
    self.speak = speak

  #create name method
  def name(self):
    return self.name

  #create age method
  def age(self):
    return self.age

  #create race method
  def race(self):
    return self.race

  #create weight method
  def weight(self):
    return self.weight

  #create speak method
  def speak(self):
    return self.speak

  #create class method change language
  @classmethod
  def change_language(cls, new_language):
    cls.language = new_language
    return new_language

  #create static method to print "im human"
  @staticmethod
  def speaklife():
    print("Im Human")

h1 = Human("Nathan", 19, "Black", 178, "Aloha")
print(h1.language)
h1.language = "spanish"
print(h1.language)
h1.speaklife()
