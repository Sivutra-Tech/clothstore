from warehouse import warehouse
wh = warehouse()

while True:
    userChoice = input("What do you want to purchase? Shoe? Pant? Shirt? : ")
    if userChoice.lower() == "Shoe".lower():
        wh.print("Shoe")
        break
    elif userChoice.lower() == "Pant".lower():
        wh.print("Pant")
        break
    elif userChoice.lower() == "Shirt".lower():
        wh.print("Shirt")
        break
    else:
        print("Error! Try Again")
    
while True:
    try:
        ID = int(input("What do you like to purchase? ID: "))
        if isinstance(ID,int) and wh.check_ID(ID,userChoice):
            break
        else:
            print("Wrong ID, Please Try Again!")
    except:
        print("Error! Try Again!")

if userChoice.lower() == "shoe":
        price = wh.get_shoe_price(ID)
        print(f"Your price is ${price}")
if userChoice.lower() == "pant":
        price = wh.get_pant_price(ID)
        print(f"Your price is ${price}")
if userChoice.lower() == "shirt":
        price = wh.get_shirt_price(ID)
        print(f"Your price is ${price}")

while True:
    yesOrNo = input("Do you have a membership? Y/N: ")
    if yesOrNo.lower() == "y" or yesOrNo == "yes":
         BREAK=False
         while True:
              try:
                   choice = int(input("What tier is your Membership? 1,2 or 3? : "))
                   if choice == 1:
                    price = int(price)
                    price *= 0.75
                    print(f"Your discounted price is ${price}")
                    BREAK = True
                    break
                   elif choice == 2:
                    price = int(price)
                    price *= 0.5
                    print(f"Your discounted price is ${price}")
                    BREAK = True
                    break
                   elif choice == 3:
                    price = int(price)
                    price *= 0.25
                    print(f"Your discounted price is ${price}") 
                    BREAK = True
                    break 
              except:
                  print("Error! Try Again!")
         if BREAK:
             break
    elif yesOrNo.lower() == "n" or yesOrNo == "yes":
         print(f"Your price is ${price}")
         break
        

choice = input("How do you like to pay? cash or card?")

print("Recieved, Thank you for coming")

wh.purchase_log(ID,price)


