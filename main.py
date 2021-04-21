import functools

global num
global list1
global list2
global result
global inputs

def main():
    num = float(input("Enter a number: "))
    list1.append(num)
    
    while num != 0:
        num = float(input("Enter another number: "))
        if num != 0:
            list1.append(num)
    return list1

def addNums():
    result = 0
    for addNum in list1:
        result += addNum
    
    return [result]

def subNums():
    result = functools.reduce(lambda a, b: a-b, list1)
    inputs = len(list1)
        
    return [result, inputs]

def prodNums():
    result = 1
    for prodNum in list1:
        result *= prodNum
        
    return [result]

def divNums():
    result = functools.reduce(lambda a, b: a/b, list1)
    inputs = len(list1)
        
    return [result, inputs]

def average():
    result = 0
    for avNum in list1:
        result += avNum
    length = len(list1)
    result = result / length
    
    return [result, length]

print("Before you start, i want to tell you that")
print("this is a super complicated calculator and i")
print("wasted way too much time in debugging it. Please")
print("support me by starring this file.")
print("")

while True:
    print("\n")
    print("New type of calculator by me")
    print("[1] Addition")
    print("[2] Subtraction")
    print("[3] Multiplication")
    print("[4] Division")
    print("[5] Average")
    print("[6] Quit")
    c = int(input(''))
    list1 = []
    
    if c != 6:
        if c == 1:
            main()
            list2 = addNums()
            length = len(list1)
            print("Result: {}    Inputs: {}".format(list2[0], length))
            print("")
        elif c == 2:
            main()
            list2 = subNums()
            print("Result: {}    Inputs: {}".format(list2[0], list2[1]))
            print("")
        elif c == 3:
            main()
            list2 = prodNums()
            length = len(list1)
            print("Result: {}    Inputs: {}".format(list2[0], length))
            print("")
        elif c == 4:
            main()
            list2 = divNums()
            print("Result: {}    Inputs: {}".format(list2[0], list2[1]))
            print("")
        elif c == 5:
            main()
            list2 = average()
            print("Result: {}    Inputs: {}".format(list2[0], list2[1]))
            print("")
    else:
        print("Ok bye!")
        break
    
