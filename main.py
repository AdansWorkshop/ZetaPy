import random

command = input("zetapy> ")
filename = ""
file = None
fileContents = []
stack = {}
filename = command
file = open(filename, "r")
print("\n------------------------------------------------------------------\n")
if not file == None:
    fileContents = file.read().split("\n")
    for i in range(0, len(fileContents)):
        lineWords = fileContents[i].split(" ")
        for j in range(0, len(lineWords)):
            if lineWords[j] == "out":
                if lineWords[j + 1] in stack.keys():
                    print(stack.get(lineWords[j + 1]))
                elif lineWords[j + 1] == "+":
                    a = None
                    b = None
                    if lineWords[j + 2] in stack.keys():
                        a = stack.get(lineWords[j + 2])
                    elif lineWords[j + 2].isnumeric():
                        a = float(lineWords[j + 2])
                    if lineWords[j + 3] in stack.keys():
                        b = stack.get(lineWords[j + 3])
                    elif lineWords[j + 3].isnumeric():
                        b = float(lineWords[j + 3])
                    if not a == None and not b == None:
                        print(a + b)
                elif lineWords[j + 1] == "-":
                    a = None
                    b = None
                    if lineWords[j + 2] in stack.keys():
                        a = stack.get(lineWords[j + 2])
                    elif lineWords[j + 2].isnumeric():
                        a = float(lineWords[j + 2])
                    if lineWords[j + 3] in stack.keys():
                        b = stack.get(lineWords[j + 3])
                    elif lineWords[j + 3].isnumeric():
                        b = float(lineWords[j + 3])
                    if not a == None and not b == None:
                        print(a - b)
                elif lineWords[j + 1] == "*":
                    a = None
                    b = None
                    if lineWords[j + 2] in stack.keys():
                        a = stack.get(lineWords[j + 2])
                    elif lineWords[j + 2].isnumeric():
                        a = float(lineWords[j + 2])
                    if lineWords[j + 3] in stack.keys():
                        b = stack.get(lineWords[j + 3])
                    elif lineWords[j + 3].isnumeric():
                        b = float(lineWords[j + 3])
                    if not a == None and not b == None:
                        print(float(a) * float(b))
                elif lineWords[j + 1] == "/":
                    a = None
                    b = None
                    if lineWords[j + 2] in stack.keys():
                        a = stack.get(lineWords[j + 2])
                    elif lineWords[j + 2].isnumeric():
                        a = float(lineWords[j + 2])
                    if lineWords[j + 3] in stack.keys():
                        b = stack.get(lineWords[j + 3])
                    elif lineWords[j + 3].isnumeric():
                        b = float(lineWords[j + 3])
                    if not a == None and not b == None:
                        print(float(a) / float(b))
                elif lineWords[j + 1] == "**":
                    if lineWords[j + 2] in stack.keys():
                        print(float(stack.get(lineWords[j + 2])) ** 2)
                    elif lineWords[j + 2].isnumeric():
                        print(float(lineWords[j + 2]) ** 2)
                elif lineWords[j + 1] == "***":
                    if lineWords[j + 2] in stack.keys():
                        print(float(stack.get(lineWords[j + 2])) ** 3)
                    elif lineWords[j + 2].isnumeric():
                        print(float(lineWords[j + 2]) ** 3)
                elif lineWords[j + 1] == "sqrt":
                    if lineWords[j + 2] in stack.keys():
                        print(float(stack.get(lineWords[j + 2])) ** .5)
                    elif lineWords[j + 2].isnumeric():
                        print(float(lineWords[j + 2]) ** .5)
                elif lineWords[j + 1] == "cbrt":
                    if lineWords[j + 2] in stack.keys():
                        print(float(stack.get(lineWords[j + 2])) ** (1/3))
                    elif lineWords[j + 2].isnumeric():
                        print(float(lineWords[j + 2]) ** (1/3))
                else: 
                    print(fileContents[i].split("out ")[1])
            if lineWords[j] == "in":
                stack[lineWords[j + 1]] = input()
            if lineWords[j] == "set":
                if lineWords[j + 2] == "rand":
                    stack[lineWords[j + 1]] = random.randint(int(lineWords[j + 3]), int(lineWords[j + 4]))
                elif lineWords[j + 2] == "iter":
                    list = []
                    for k in range(3, len(fileContents[i].split(" "))):
                        list.append(lineWords[k])
                    stack[lineWords[j + 1]] = list
                else:
                    if lineWords[j + 2].isnumeric():
                        stack[lineWords[j + 1]] = float(lineWords[j + 2])
                    else:
                        stack[lineWords[j + 1]] = lineWords[j + 2]
            if lineWords[j] == "unset":
                stack.pop(lineWords[j + 1])
            if lineWords[j] == "+=":
                if lineWords[j + 1] in stack.keys():
                    stack[lineWords[j - 1]] += stack.get(lineWords[j + 1])
                else:
                    stack[lineWords[j - 1]] += float(lineWords[j + 1])
            if lineWords[j] == "-=":
                if lineWords[j + 1] in stack.keys():
                    stack[lineWords[j - 1]] -= stack.get(lineWords[j + 1])
                else:
                    stack[lineWords[j - 1]] -= float(lineWords[j + 1])
            if lineWords[j] == "*=":
                if lineWords[j + 1] in stack.keys():
                    stack[lineWords[j - 1]] *= stack.get(lineWords[j + 1])
                else:
                    stack[lineWords[j - 1]] *= float(lineWords[j + 1])
            if lineWords[j] == "/=":
                if lineWords[j + 1] in stack.keys():
                    stack[lineWords[j - 1]] /= stack.get(lineWords[j + 1])
                else:
                    stack[lineWords[j - 1]] /= float(lineWords[j + 1])
            
            