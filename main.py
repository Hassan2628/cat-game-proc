
import os
cat_attributes = {
    "intelligence": 50,
    "energy": 100,
    "weight": 50,
    # change the inital values above
}

print("Welcome to my cat game!")

# Take the user inputs for name and colour:
name = input("Enter the name of your cat:")
colour = input("Enter the colour of your cat:")

# start the while loop
while True:
    # Finish the string below
    option = input("What would you like to do? 1. Play with your cat 2. Train your cat 3. Feed your cat 4. Put your cat to sleep 5. show stats ")

    if option == '1':
        # change the cat's attributes here
       os.system("clear")
       cat_attributes["energy"] += -10
       cat_attributes["intelligence"] += 5
       cat_attributes["weight"] += -5
       print(cat_attributes)
    elif option == '2':
       os.system("clear")
       cat_attributes["energy"] += -20
       cat_attributes["intelligence"] += 10
       cat_attributes["weight"] += -10
       print(cat_attributes)
    elif option == '3':
       os.system("clear")
       cat_attributes["energy"] += 10
       cat_attributes["intelligence"] += -7
       cat_attributes["weight"] += 10
       print(cat_attributes) 
    elif option == '4':
       os.system("clear")
       cat_attributes["energy"] += 15
       cat_attributes["intelligence"] += -5
       cat_attributes["weight"] += 5
       print(cat_attributes)  
    elif option == '5': 
        os.system("clear")    
        print(cat_attributes)
        
    # elif ...
    else:
       os.system("clear")
       print("Please pick an option.")

        

    # finish off the if statements below
    if cat_attributes['energy'] < 5:
        os.system("clear")
        print("Your cat has died and the game has ended, better luck next time.")
        print(cat_attributes)
        break
    # elif ...