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


class Numbers:
    def __init__(self,a=0,b=0):
      self.a = a
      self.b = b

    def __add__(self,other):
      a = self.a + other.a
      b = self.b + other.b
      return a+b
       

a = Numbers(0,0)
b= Numbers(9,5)
print(a.__add__(b))

pdict = {
  "josh": 40,
  "adam": 50
}

pdict["josh"] = 90
for x,y in pdict.items():
  print(x, y)
