# integer=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
# roman=["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
# val=int(input("Enter a value:"))
# rst=""
# for i in range(len(integer)):
#     while val>=integer[i]:
#         rst+=roman[i]
#         val-=integer[i]
# print(rst)


class RomConv:
    def __init__(self):
        self.integer=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
        self.roman=["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        