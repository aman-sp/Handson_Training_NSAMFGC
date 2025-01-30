n=int(input("Enter the number of possible demands: "))
for i in range(n):
    li=int(input("\nEnter the required liters of milk: "))
    bot=0
    while li!=0:
        if li>=10:
            bot+=li//10
            li%=10
        elif li>=5:
            bot+=li//5
            li%=5
        else:
            bot+=li
            li=0
    print("The milk will be packed in", bot, "bottles.")