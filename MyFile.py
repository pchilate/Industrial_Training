def fibo(term):
    a,b = 0,1

    while a < term:
        print(a)

        a,b = b,a+b


n = int(input("Enter the term: "))
fibo(n)