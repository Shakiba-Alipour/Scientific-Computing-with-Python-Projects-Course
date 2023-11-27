def arithmetic_arranger(array, solution):
    if len(array) > 5:
        print("Error: Too many problems.")

    results, operators, firstOperands, secondOperands = []

    for item in array:
        items = item.split(" ")
        if items[1] == "+" | items[1] == "-":
            if items[0].isdigit() & items[2].isdigit():
                firstOperands.append(items[0])
                secondOperands.append(items[2])
                # + would be 0 and - would be 1
                if items[1] == "+":
                    operators.append(0)
                else:
                    operators.append(1)
            else:
                print("Error: Numbers must only contain digits.")
        else:
            print("Error: Operator must be " + " or " - ".")

    # solve the problems
    if solution:
        i = 0
        while i < len(array):
            if operators[i] == 0:
                results.append(firstOperands[i] + secondOperands[i])
            else:
                results.append(firstOperands[i] - secondOperands[i])
            i += 1

    # print the problems
    # length of each printed problem
    lengths = []
    # print first line
    i = 0
    while i < len(array):
        firstOperandLen = len(str(firstOperands[i]))
        secondOperandLen = len(str(secondOperands[i]))

        if firstOperandLen >= secondOperandLen:
            lengths.append(2 + firstOperandLen)
            print("  " + firstOperands[i], end="    ")
        else:
            lengths.append(2 + secondOperandLen)
            j = 0
            while j < (secondOperandLen + 2 - firstOperandLen):
                print(" ", end="")
                j += 1
            print(firstOperands[i], end="    ")

        i += 1

    print()

    # print second line
    i = 0
    while i < len(array):
        firstOperandLen = len(str(firstOperands[i]))
        secondOperandLen = len(str(secondOperands[i]))

        if operators[i] == 0:
            print("+ ", end="")
        else:
            print("- ", end="")

        if firstOperandLen >= secondOperandLen:
            print(secondOperands[i], end="    ")
        else:
            j = 0
            while j < (firstOperandLen + 2 - secondOperandLen):
                print(" ", end="")
                j += 1
            print(secondOperands[i], end="    ")

        i += 1

    print()

    # print third line
    i = 0
    while i < len(array):
        j = 0
        while j < lengths[i]:
            print("-", end="")
        print("    ", end="")

        i += 1

    print()

    # print results
    if solution:
        i = 0
        while i < len(array):
            j = 0
            while j < lengths[i] - len(str(results[i])):
                print(" ", end="")

            print(results[i] + "    ", end="")
            i += 1
