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

#add,subtract,multiply,divide functions program
#create an introduction/instruction function
def instructions():
  print("You are to type two numbers and the following operations will be performed:(multiplication,division,addition,subtraction")



#create input of two nums function
def input_nums():
  global num1 
  global num2
  try:
    num1 = int(input("Type in the 1st number: "))
    num2 = int(input("Type in the 2nd number: "))
  except ValueError:
    print("Looks like you typed something incorrect!")

#create add function
def add():
  return num1 + num2

#create subtraction function
def subtract():
  return num2 - num1

#create multiplication function
def mult():
  return num1 * num2

#create division function
def div():
  return num2 / num1

instructions()
input_nums()
print(add())
print(subtract())
print(mult())
print(div())
