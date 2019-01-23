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

#number guess program

#import random library
import random
replay = True

#prompt the user and give them instructions
print("You will try to guess the computers number by typing one in")
#create a while loop
while replay:
  #create a random variable with range 1-10
  rand = random.randint(1,10)
  #have user type in the number
  print("The computer has selected a number")
  try:
    num = int(input("Now enter a number: "))
  except ValueError:
    print("Looks like you typed something incorrect!")
  #check if number matches
  if rand == num:
    print("You got it!")
  else:
    #print out the random number
    print("Sorry you didnt quite get it, the number was: ", rand)
  #ask to play again, if not exit
  play = int(input("Would you like to replay?(1=yes,2=no): "))
  if play == 1:
    continue
  elif play == 2:
    print("Adios!")
    replay = False
