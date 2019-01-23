#fizzbuzz program, check for even / odd numbers


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



print("Lets play some fizz-buzz")
print("If the number is even, ill say fizz, if its odd, ill say buzz")

play = True

try:
  while play:
    num = int(input("Enter a number here to start: "))
    if num % 2 == 0:
      print("fizz")
    else:
      print("buzz")
    try:
      ans = int(input("Would you like to play again?(1=yes,2=no): "))
      if ans == 1:
        continue
      elif ans == 2:
        play = False
        print("Goodbye!")
    except ValueError:
      print("ERROR")
    
except ValueError:
  print("Looks like you typed something incorrect!")
