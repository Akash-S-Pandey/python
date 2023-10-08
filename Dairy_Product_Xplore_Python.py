class DairyProduct:
    def __init__(self,id,brand,ptype,price,grade) -> None:
        self.id = id
        self.brand = brand
        self.ptype=ptype
        self.price=price
        self.grade=grade
class productGrade:
    def __init__(self,dairyList,weightagedict) -> None:
        self.dairyList = dairyList
        self.weightagedict = weightagedict
    def priceBasedOnBrandAndType(self,dbrand,prodtype):
        for i in self.dairyList:
            if (i.brand.lower() == dbrand.lower()) and i.ptype.lower() == prodtype.lower():
                updated_price = (i.price + i.price*self.weightagedict[i.grade]/100)
                i.price = updated_price
                return i
        return None


def main():
    list_prod=[]
    for i in range(int(input())):
        id=int(input())
        brand = input()
        ptype = input()
        price = int(input())
        grade = input()
        list_prod.append(DairyProduct(id,brand,ptype,price,grade))
    grades={}
    for i in range(int(input())):
        x=input()
        y=int(input())
        grades[x]=y
    dbrand = input()
    ptype = input()
    p = productGrade(list_prod,grades)
    res = p.priceBasedOnBrandAndType(dbrand,ptype)
    if res == None:
        print("No dairy product found")
    else:
        print("Dairy Brand: "+str(res.brand))
        print("Price: "+str(res.price))

main()