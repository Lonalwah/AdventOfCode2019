#! python3

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
        #Get Instruction Values
        opcode = intCode[insPtr]
        
        # For debugging
        # print('Instruction Pointer: %s\tOpcode: %s' % (insPtr, opcode))
        p1 = getParamValue(insPtr + 1, intCode)
        p2 = getParamValue(insPtr + 2, intCode)
        p3 = intCode[insPtr + 3]

        if p3 > len(intCode)-1:
            print('break', p3)

        #Process Instruction
        if(opcode == 1):    # Add
            intCode[p3] = p1 + p2
            step = 4
        elif(opcode == 2):  # Mul
            intCode[p3] = p1 * p2
            step = 4
        elif(opcode == 99): # Exit
            step = 1
            break

        insPtr += step
    return intCode

def partOne():
    print('Part 1')
    f = open("input.txt", "r")
    code = f.read()
    f.close()

    code = [int(i) for i in code.split(",")]
    code[1] = 12
    code[2] = 2

    output = processIntcode(code)[0]
    print('Output is %s' % output)

def partTwo(targetOutput):
    print('Part 2')

    f = open("input.txt", "r")
    code_orig = f.read()
    code_orig = [int(i) for i in code_orig.split(",")]
    f.close()

    for noun in range(0, 100):
        for verb in range(0, 100):
            # Restart Code
            code = code_orig.copy()
            code[1] = noun
            code[2] = verb
            
            output = processIntcode(code)[0]

            if (output == targetOutput): 
                break
        else:
            continue
        break

    
    print('Output is %s' % output)
    print('Noun: %s\t Verb: %s' % (noun, verb))
    print('Anwser: %i' % (100 * noun + verb))


partOne()
partTwo(19690720)
