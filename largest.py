highestnum = 0 
# intiate highestnum variable as 0 


for i in range(0, 4, 1):
    userinput("Number please...")
    userInt = int(userinput)
    print("User entered:" + str(userinput))
    if userInt > highestnum:
        highestnum = userInt
        print("Upadting highest number...")
        else:
          print("This is not the highest number!")
    print("The highest number entered is:" + str(highestnum))

    
       
