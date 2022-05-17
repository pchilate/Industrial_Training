n = int(input("Enter the no. of scroes: "))
arr =map(int, input("Enter all the scores: ").split())

arr = list(set(arr))

def runnerup(arr):
    return sorted(arr)[-2]


print(runnerup(arr))