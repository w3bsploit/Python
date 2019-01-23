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

#name,age, into one sentence program

#create instructions function
def instructions():
  print("You are to enter your name and age, a custom greeting will outputted.")

#create name input function
def get_name():
  try:
    name = input("Enter your name to begin: ")
  except ValueError:
    print("Looks like you typed something incorrect!")
  return name

#create age input function
def get_age():
  try:
    age = int(input("Enter your age: "))
  except ValueError:
    print("Looks like you typed something incorrect!")
  return age

#create sentence function
def sentence():
  return "Your name is: " + get_name() + " and you are: " + str(get_age()) + "years old." + "Delighted to meet you!"

instructions()
print(sentence())
