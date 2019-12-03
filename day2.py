#! python3

code = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,6,19,23,1,10,23,27,2,27,13,31,1,31,6,35,2,6,35,39,1,39,5,43,1,6,43,47,2,6,47,51,1,51,5,55,2,55,9,59,1,6,59,63,1,9,63,67,1,67,10,71,2,9,71,75,1,6,75,79,1,5,79,83,2,83,10,87,1,87,5,91,1,91,9,95,1,6,95,99,2,99,10,103,1,103,5,107,2,107,6,111,1,111,5,115,1,9,115,119,2,119,10,123,1,6,123,127,2,13,127,131,1,131,6,135,1,135,10,139,1,13,139,143,1,143,13,147,1,5,147,151,1,151,2,155,1,155,5,0,99,2,0,14,0]

def getParamValue(address, intCode):
    value = -1
    pointer = intCode[address]

    if pointer <= len(intCode)-1:
        value = intCode[pointer]

    return value

def processIntcode(intCode):
    #Get Instruction Pointer/Address
    insPtr = 0
    step = 1

    while(insPtr < len(intCode)-1):
        print('\r%s' % step, end='')
        #Get Instruction Values
        opcode = intCode[insPtr]
        p1 = getParamValue(insPtr + 1, intCode)
        p2 = getParamValue(insPtr + 2, intCode)
        p3 = intCode[insPtr + 3]

        if p3 > len(intCode)-1:
            print('break', p3)

        #Process Instruction
        if(opcode == 1):
            intCode[p3] = p1 + p2
            step = 4
        elif(opcode == 2):
            intCode[p3] = p1 * p2
            step = 4
        elif(opcode == 99):
            step = 1
            break

        insPtr += step
    return intCode

def setIntcodeNounVerb(intCode, noun, verb):
    newCode = intCode
    print(newCode)
    newCode[1] = noun
    newCode[2] = verb
    return newCode

def partTwo():
    for n in range(0,99):
        for v in range(0,99):
            print(n,v)
            output = processIntcode(setIntcodeNounVerb(code, n, v))[0]

            if output == 19690720:
                break
    print('Output is %s' % output)
    print('Answer is %s' % (100 * n + v))

def partOne():
    noun = 12
    verb = 2
    output = processIntcode(setIntcodeNounVerb(code, noun, verb))[0]

    print('Output is %s' % output)
    print('Answer is %s' % (100 * noun + verb))

partTwo()