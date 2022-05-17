# Here you can fine the runnerup score
# offer closes soooon!!!11

n = int(input("Enter the no. of scroes: "))
arr =map(int, input("Enter all the scores: ").split())

arr = list(set(arr))

def runnerup(arr):
    return sorted(arr)[-2]


print("The runnerup score is: ",runnerup(arr))