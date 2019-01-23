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
#counting program

try:
  starting = int(input("Enter the number youd like to start with: "))
  ending = int(input("Enter the number youd like to count to: "))
except ValueError:
  print("Oops! Looks like you typed something incorrect!")

for x in range(starting,ending+1):
  print(x)
