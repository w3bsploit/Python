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

#string controlled loop program
#create a boolean variable to continue/stop the loop
reloop = True

#create a loop
while reloop:
  #have the user type stuff in
  try:
    string = str(input("type in a string: "))
      #check if its a number, if so exit the loop, otherwise continue
    if (string.isdigit()):
      print("thats not a string!")
      reloop = False
    else:
      continue
  except ValueError:
    print("looks like you typed something incorrect!")
