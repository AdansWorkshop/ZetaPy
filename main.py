command = input()
filename = ""
file = None
fileContents = []
stack = {}
if command.split(" ")[0] == "zetapy":
    filename = command.split(" ")[1]
    file = open(filename, "r")
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
                    if lineWords[j + 3] in stack.keys():
                        b = stack.get(lineWords[j + 3])
                    if not a == None and not b == None:
                        print(float(a) + float(b))
                    elif not a == None:
                        print(a + lineWords[j + 3])
                    elif not b == None:
                        print(lineWords[j + 2] + b)
                elif lineWords[j + 1] == "-":
                    if lineWords[j + 2] in stack.keys() and lineWords[j + 3] in stack.keys():
                        print(float(stack.get(lineWords[j + 2])) - float(stack.get(lineWords[j + 3])))
                elif lineWords[j + 1] == "*":
                    if lineWords[j + 2] in stack.keys() and lineWords[j + 3] in stack.keys():
                        print(float(stack.get(lineWords[j + 2])) * float(stack.get(lineWords[j + 3])))
                elif lineWords[j + 1] == "/":
                    if lineWords[j + 2] in stack.keys() and lineWords[j + 3] in stack.keys():
                        print(float(stack.get(lineWords[j + 2])) / float(stack.get(lineWords[j + 3])))
                elif lineWords[j + 1] == "**":
                    if lineWords[j + 2] in stack.keys():
                        print(float(stack.get(lineWords[j + 2])) ** 2)
                elif lineWords[j + 1] == "***":
                    if lineWords[j + 2] in stack.keys():
                        print(float(stack.get(lineWords[j + 2])) ** 3)
                else:
                    print(fileContents[i].split("out ")[1])
            if lineWords[j] == "in":
                stack[lineWords[j + 1]] = input()
            if lineWords[j] == "set":
                stack[lineWords[j + 1]] = lineWords[j + 2]

        