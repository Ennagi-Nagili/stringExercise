a = input()
number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
           't', 'u', 'v', 'w', 'x', 'y', 'z']
result = ""
result1 = 0
for i in a:
    for j in number:
        if i == str(j):
            result += str(j)
            break

        else:
            for t in letters:
                if i == t:
                    if result != "":
                        result1 += int(result)
                    result = ""
                    break

print(result1)