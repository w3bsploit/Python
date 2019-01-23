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
#name - age dictionary program

#start by making a dictionary with names and ages
name_age = {"John Ashton": 25, "Ashley Andrade": 20, "Lilly petal": 35, "Nathan Heath": 19}

#create a function to print out the dictionary
def print_dict():
  for key,value in name_age.items():
    print(key,"---",value)

#create a function to add to the dictionary
def add_dict():
  try:
    name = input("Type in a name: ")
    age = int(input("Type in their age: "))
  except ValueError:
    print("Opps! Looks like you typed something incorrect!")
  name_age[name] = age

#create a function to remove from the dictionary
def remove_dict():
  #see if name exists in dict
  try:
    existing = input("Enter a name you'd like to remove: ")
    print("searching...")
    for key,value in name_age.items():
      if existing not in name_age:
        print("Looks like the name is not in this list!")
      else:
        print("Name found!")
        option = int(input("Would you like to delete? (1=yes, 2=no): "))
        if option == 1:
          del name_age[existing]
          break
        elif option == 2:
          continue

  except ValueError:
    print("Opps! Looks like you typed something incorrect!")

#create a function that prints the updated dictionary
def print_updated():
  for key,value in name_age.items():
    print(key,"----",value)

print_dict()
add_dict()
remove_dict()
print_updated()
