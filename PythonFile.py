n = 5
arr = [10,25,36,89,56]

arr = list(set(arr))

def runnerup(arr):
    return sorted(arr)[-2]


print(runnerup(arr))