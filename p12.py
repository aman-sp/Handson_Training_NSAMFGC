
class RomConv:
    def __init__(self):
        self.integer=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
        self.roman=["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
    def ToRom(self,val):
        rst=""
        for i in range(len(self.integer)):
            while val>=self.integer[i]:
                rst+=self.roman[i]
                val-=self.integer[i]
        return rst
conv=RomConv()
val=int(input("Enter a value:"))
print("Roman Value:",conv.ToRom(val))