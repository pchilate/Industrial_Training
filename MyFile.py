# def fibo(term):
#     a,b = 0,1

#     while a < term:
#         print(a)

#         a,b = b,a+b


# n = int(input("Enter the term: "))
# fibo(n)

def swap(c):
    if c.islower():
        return c.upper()
    else:
        return c.lower()



def swap_case(s):
    return "".join(map(swap , s))


print(swap_case("Hello World"))