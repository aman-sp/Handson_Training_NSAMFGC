class DOp:
    def __init__(self,n):
        self.n=n
        self.num=[]
    def cal_pair_sum(self):
        while self.n>0:
            digit=self.n % 10
            self.num.append(digit)
            self.n=self.n//10
        self.num.sort(reverse=True)
        sum=0
        for i in range(len(self.num)):
            j=i+1
            while j<len(self.num):
                print(f"({self.num[i]}+{self.num[j]})+",end="")
                sum+=self.num[i]+self.num[j]
                j+=1
        print(":",sum)
class SumCal(DOp):
    def __init__(self,n):
        self.n=n
        self.num=[]
    def calculate(self):
        self.cal_pair_sum()
n=int(input("Enter the Digits:"))
cal=SumCal(n)
cal.calculate()