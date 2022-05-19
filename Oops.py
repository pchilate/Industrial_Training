

class Land:
    def __init__(self, name, length , breadth , sqftprice):
        self.name = name
        self.length = length
        self.breadth = breadth
        self.sqftprice = sqftprice


    def __str__(self):
        return str(self.__name__) + "\n" +  str(self.length) + "\n" + str(self.breadth)



name   = input("Enter the land name: ")
len , brh , sqftprice =  map(float , input("Enter length , breadth and sqft price: ").split())

land = Land(name,len,brh,sqftprice)


print(land)




























