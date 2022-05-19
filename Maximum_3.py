# function to find Maximum among three

def Maximum_of_Three(a,b,c):
    result = a if a > b  and a > c else b if b > c  else c
    return result


n1,n2,n3 = map(float,(input("Enter three numbers to find maximum: ").split()))

print(Maximum_of_Three(n1,n2,n3))