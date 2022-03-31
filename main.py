import random
from typing import List

command = input("zetapy> ")
filename = ""
file = None
fileContents = []
stack = {}
filename = command
file = open(filename, "r")
print("\n------------------------------------------------------------------\n")

def set(lineWords, line, args, stack, j):
    if lineWords[j + 2] == "rand":
        stack[lineWords[j + 1]] = random.randint(int(lineWords[j + 3]), int(lineWords[j + 4]))
    elif lineWords[j + 2] == "iter":
        list = []
        for k in range(3, len(line.split(" "))):
            if lineWords[k].isnumeric():
                list.append(float(lineWords[k]))
            elif lineWords[k] == "args":
                list.append(args)
            else:
                list.append(lineWords[k])
        stack[lineWords[j + 1]] = list
    else:
        if lineWords[j + 2].isnumeric():
            stack[lineWords[j + 1]] = float(lineWords[j + 2])
        else:
            stack[lineWords[j + 1]] = lineWords[j + 2]
def unset(lineWords, stack, i, j):
    stack.pop(lineWords[j + 1])
def setin(lineWords, stack, i, j):
    stack[lineWords[j + 1]] = input()
def out(lineWords, line, stack, j, args):
    if lineWords[j + 1] in stack.keys():
        print(stack.get(lineWords[j + 1]))
    elif lineWords[j + 1] == "+":
        a = None
        b = None
        if lineWords[j + 2] in stack.keys():
            a = stack.get(lineWords[j + 2])
        elif lineWords[j + 2] == "args":
            a = args
        elif lineWords[j + 2].isnumeric():
            a = float(lineWords[j + 2])
        if lineWords[j + 3] in stack.keys():
            b = stack.get(lineWords[j + 3])
        elif lineWords[j + 3] == "args":
            b = args
        elif lineWords[j + 3].isnumeric():
            b = float(lineWords[j + 3])
        if not a == None and not b == None:
            print(a + b)
    elif lineWords[j + 1] == "-":
        a = None
        b = None
        if lineWords[j + 2] in stack.keys():
            a = stack.get(lineWords[j + 2])
        elif lineWords[j + 2] == "args":
            a = args
        elif lineWords[j + 2].isnumeric():
            a = float(lineWords[j + 2])
        if lineWords[j + 3] in stack.keys():
            b = stack.get(lineWords[j + 3])
        elif lineWords[j + 3] == "args":
            b = args
        elif lineWords[j + 3].isnumeric():
            b = float(lineWords[j + 3])
        if not a == None and not b == None:
            print(a - b)
    elif lineWords[j + 1] == "*":
        a = None
        b = None
        if lineWords[j + 2] in stack.keys():
            a = stack.get(lineWords[j + 2])
        elif lineWords[j + 2] == "args":
            a = args
        elif lineWords[j + 2].isnumeric():
            a = float(lineWords[j + 2])
        if lineWords[j + 3] in stack.keys():
            b = stack.get(lineWords[j + 3])
        elif lineWords[j + 3] == "args":
            b = args
        elif lineWords[j + 3].isnumeric():
            b = float(lineWords[j + 3])
        if not a == None and not b == None:
            print(float(a) * float(b))
    elif lineWords[j + 1] == "/":
        a = None
        b = None
        if lineWords[j + 2] in stack.keys():
            a = stack.get(lineWords[j + 2])
        elif lineWords[j + 2] == "args":
            a = args
        elif lineWords[j + 2].isnumeric():
            a = float(lineWords[j + 2])
        if lineWords[j + 3] in stack.keys():
            b = stack.get(lineWords[j + 3])
        elif lineWords[j + 3] == "args":
            b = args
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
    elif lineWords[j + 1] == "args" and not args == None:
        print(args)
    elif lineWords[j + 1] != "args": 
        print(line.split("out ")[1])
def adde(lineWords, stack, j):
    if lineWords[j + 1] in stack.keys():
        stack[lineWords[j - 1]] += stack.get(lineWords[j + 1])
    else:
        stack[lineWords[j - 1]] += float(lineWords[j + 1])
def sube(lineWords, stack, j):
    if lineWords[j + 1] in stack.keys():
        stack[lineWords[j - 1]] -= stack.get(lineWords[j + 1])
    else:
        stack[lineWords[j - 1]] -= float(lineWords[j + 1])
def multe(lineWords, stack, j):
    if lineWords[j + 1] in stack.keys():
        stack[lineWords[j - 1]] *= stack.get(lineWords[j + 1])
    else:
        stack[lineWords[j - 1]] *= float(lineWords[j + 1])
def dive(lineWords, stack, j):
    if lineWords[j + 1] in stack.keys():
        stack[lineWords[j - 1]] /= stack.get(lineWords[j + 1])
    else:
        stack[lineWords[j - 1]] /= float(lineWords[j + 1])
def each(lineWords, line, stack, j):
    if lineWords[j + 1] in stack.keys():
        iter = stack.get(lineWords[j + 1])
        if isinstance(iter, list):
            for k in range(0, len(iter)):
                rest_of_line = line[2:]
                parse(rest_of_line, iter[k])
def add(lineWords, args, stack, j):
    if lineWords[j - 1] in stack:
        iter = stack.get(lineWords[j - 1])
        if isinstance(iter, list):
            if lineWords[j + 1].isnumeric():
                iter.append(float(lineWords[j + 1]))
            elif lineWords[j + 1] == "args":
                iter.append(args)
            elif lineWords[j + 2] == "index":
                if lineWords[j + 1] in stack.keys():
                    iter1 = stack.get(lineWords[j + 1])
                    if isinstance(iter1, list):
                        if lineWords[j + 3] == "args" and not args == None:
                            iter.append(iter1[args])
                        else:
                            iter.append(iter1[int(lineWords[j + 3])])
            else:
                iter.append(lineWords[j + 1])
            stack[lineWords[j - 1]] = iter
def rem(lineWords, args, stack, j):
    if lineWords[j - 1] in stack:
        iter = stack.get(lineWords[j - 1])
        if isinstance(iter, list):
            if lineWords[j + 1].isnumeric():
                iter.remove(float(lineWords[j + 1]))
            elif lineWords[j + 1] == "args":
                iter.remove(args)
            elif lineWords[j + 2] == "index":
                if lineWords[j + 1] in stack.keys():
                    iter1 = stack.get(lineWords[j + 1])
                    if isinstance(iter1, list):
                        if lineWords[j + 3] == "args" and not args == None:
                            iter.remove(iter1[args])
                        else:
                            iter.remove(iter1[int(lineWords[j + 3])])
            else:
                iter.remove(lineWords[j + 1])
            stack[lineWords[j - 1]] = iter
def parse(line, args):
    lineWords = line.split(" ")
    for j in range(0, len(lineWords)):
        if lineWords[j] == "out":
            out(lineWords, line, stack, j, args)
        if lineWords[j] == "in":
            setin(lineWords, stack, j)
        if lineWords[j] == "set":
            set(lineWords, line, args, stack, j)
        if lineWords[j] == "unset":
            unset(lineWords, stack, j)
        if lineWords[j] == "+=":
            adde(lineWords, stack, j)
        if lineWords[j] == "-=":
            sube(lineWords, stack, j)
        if lineWords[j] == "*=":
            multe(lineWords, stack, j)
        if lineWords[j] == "/=":
            dive(lineWords, stack, j)
        if lineWords[j] == "each":
            each(lineWords, line, stack, j)
        if lineWords[j] == "add":
            add(lineWords, args, stack, j)
        if lineWords[j] == "rem":
            rem(lineWords, args, stack, j)
if not file == None:
    fileContents = file.read().split("\n")
    for i in range(0, len(fileContents)):
        parse(fileContents[i], None)        