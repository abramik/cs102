#14

def permutation(string):
    res = []
    for i in range(len(string)):
        if(len(string) > 1):
            for j in permutation(string[1:]):
                res.append(string[0] + j)
        else:
            return [string]
        string = string[1:] + string[0]
    return res


print(permutation(input()))
