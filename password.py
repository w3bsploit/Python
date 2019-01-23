#password requirement program

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



#greet the user
print("Greetings!")
print("Lets get set up!")

repeat = True
count = 0


#see if user typed in correct username requirements
try:
  username = str(input("Enter a username to get started: "))
except ValueError:
  print("Oops! You typed something incorrect!")

print("Lets continue!")

#see if user typed in password requirements
try:
  while repeat:
    password = input("Now type in a password.(Must be at least 8 characters, 1 special character with letters):")
    for x in password:
      count = count + 1
    if count < 8:
      print("Password is less than 8 characters, please try again")
    elif count >= 8 and '!' or '@' or '#' or '$' or '%' or '&' or '*' in password:
      print("password accepted!")
      repeat = False
    else:
      print("looks like your password doesnt have a special character, please retry")


except ValueError:
  print("Oops! You typed something incorrect!")

