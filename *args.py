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
#*args python program

#create a unlimited name storer function
def names(name1, *args):
  for arg in args:
    print(arg)

names("Nathan", "Johnathan", "Joey", "Aidan")
