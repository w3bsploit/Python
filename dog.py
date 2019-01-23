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

#instantiate dog class
class Dog:
  #initialize all instance variables
  def __init__(self, sound, speed, dogtype):
    self.sound = sound
    self.speed = speed
    self.dogtype = dogtype

  #create a sound method
  def sound(self):
    return self.sound

  #create a speed method
  def speed(self):
    return self.speed

  #create a dogtype method
  def dogtype(self):
    return self.dogtype
d1 = Dog("ruff", 9, "doberman")
print(d1.sound)
print(d1.speed)
print(d1.dogtype)


  
