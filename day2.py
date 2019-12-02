#! python3

intcode = [
    1,9,10,3,
    2,3,11,0,
    99,30,40,50]

def processIntCode(intCode):
    index = 0

    while(index < len(intCode)-1):
        opcode = intCode[index]
        if(opcode == 1):
            intCode[intCode[index+3]] = intCode[intCode[index+1]] + intCode[intCode[index+2]]
        elif(opcode == 2):
            print('Multiply')
            intCode[intCode[index+3]] = intCode[intCode[index+1]] * intCode[intCode[index+2]]
        elif(opcode == 99):
            print('Kill')
            break
        else:
            pass
        index += 4
    print(intCode)

#print(intCode)
processIntCode([1,0,0,0,99])