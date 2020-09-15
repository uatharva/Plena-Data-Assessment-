def isRepeating(string):
    new = []
    final = ''
    for i in string:
        temp = []
        temp = [i, 0]
        new.append(temp)
    string1 = string.lower()
    for j in range(len(new)):
        new[j][1] = string1.count(new[j][0].lower())
    new = sorted(new, key=lambda x: x[1])
    for j in range(len(new)):
        final += new[j][0]
    return final[0], final


x = input("Input a string: ")
print("The first letter that is not repeated and the rewritten whole string in thr order of number of occurrences is-")
print(isRepeating(x))
