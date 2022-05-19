# function to find Maximum amog two numbers

def Maximum_of_Two(a,b):
    result = a if a > b else b
    return result


n1,n2 = map(float,(input("Enter two numbers to find maximum: ").split()))

print(Maximum_of_Two(n1,n2))