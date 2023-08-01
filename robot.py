t = int(input())

instructions = []

def instructionSetter(inst):
    if((inst == "LEFT") or (inst == "RIGHT")):
        instructions.append(inst)
    else:
        i = int(inst.split()[-1]) - 1
        instructions.append(instructions[i])


def positionCalculator():
    position = 0
    for i in range(len(instructions)):
        if(instructions[i] == "LEFT"):
            position -= 1
        elif(instructions[i] == "RIGHT"):
            position += 1
    return position

for i in range(t):
    tt = int(input())
    for i in range(tt):
        inst = input()
        instructionSetter(inst)

    print(positionCalculator())
    instructions = []