# def func(value):
#   if value % 3 == 0 and value % 7 == 0:
#       return "tiktok"
#   if value % 3 == 0:
#       return "tik"
#   if value % 7 == 0:
#       return "tok"
#   return value



# n = int(input("Enter you number: "))
# print(func(n))




# function to find Maximum amog two numbers

def Maximum_of_Two(a,b):
    result = a if a > b else b
    return result


n1,n2 = map(eval,(input("Enter two numbers to find maximum: ").split()))

print(Maximum_of_Two(n1,n2))
