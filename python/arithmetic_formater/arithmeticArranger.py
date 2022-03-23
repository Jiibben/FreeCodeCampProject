
# error :
    # more than five problem

    # only addition and substraction
    # 4 digits max


#formating :
    #single space between the operator and the longest of the two operator 
    #number right aligned
    # four space between each problem
    #dashes at the bottom (whole length)



def calculateResult(tup):
    n1, n2, op = tup
    return eval(f'{n1}{op}{n2}')


def parseDataAndValidate(inputData):
    if (len(inputData)) >= 5:
        return ([], "Error: Too many problems.")
    parsedData = list()
    for data in inputData:
        n1, op, n2 = data.split()
        if (op in ["*", "/"]):
            return ([], "Error: Operator must be '+' or '-'.")
        try:
            n1int,n2int = int(n1), int(n2)
            if n1int > 9999 or n2int > 9999:
                return ([], "Error: Numbers cannot be more than four digits.")
            tup = (n1,n2,op, calculateResult((n1int, n2int, op)))
            parsedData.append(tup)
        except ValueError as e:
            return ([], "Error: Numbers must only contain digits.")
    return (parsedData, False)


def align(totalSpace, arg):
    if totalSpace == 6:
        return '{:>6}'.format(arg)
    elif totalSpace == 5:
        return '{:>5}'.format(arg)
    elif totalSpace == 4:
        return '{:>4}'.format(arg)
    elif totalSpace == 3:
        return '{:>3}'.format(arg)
    elif totalSpace == 2:
        return '{:>2}'.format(arg)
    elif totalSpace == 1:
        return '{:>1}'.format(arg)
    


def createFirstLine(data):
    a = []
    for tup in data:
        n1, n2, op, res = tup
        space = max(len(n1), len(n2)) + 1 -len(n2)
        totalSpace = max(len(n1), len(n2) + 1 + space)
        a.append(align(totalSpace,n1))
    return "    ".join(a)

def createSecondLine(data):
    a = []
    for tup in data:
        n1, n2, op, res = tup
        space = max(len(n1), len(n2)) + 1 -len(n2)
        totalSpace = max(len(n1), len(n2) + 1 + space)
        a.append(align(totalSpace,op + " " * space + n2))

    return "    ".join(a)

def createThirdLine(data):
    a = []
    for tup in data:
        n1, n2, op, res = tup
        space = max(len(n1), len(n2)) + 1 -len(n2)
        totalSpace = max(len(n1), len(n2) + 1 + space)
        a.append(align(totalSpace,"-"*totalSpace))

    return "    ".join(a)

def createFourthLine(data):
    a = []
    for tup in data:
        n1, n2, op, res = tup
        space = max(len(n1), len(n2)) + 1 -len(n2)
        totalSpace = max(len(n1), len(n2) + 1 + space)
        a.append(align(totalSpace,res))

    return "    ".join(a)

def arithmetic_arranger(problems, showAnswer):
    parsedData, error = parseDataAndValidate(problems)
    if error:
        return error


    if showAnswer:
        return f'{createFirstLine(parsedData)}\n{createSecondLine(parsedData)}\n{createThirdLine(parsedData)}\n{createFourthLine(parsedData)}'

    return f'{createFirstLine(parsedData)}\n{createSecondLine(parsedData)}\n{createThirdLine(parsedData)}'

print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
