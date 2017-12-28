def isNumber(value):
    try:
        x = float(value)
        return True
    except ValueError:
        return False

f = open("in23.txt", 'r')
instr = [x.split("\n")[0].split(" ") for x in f.readlines()]
regs = {
    "a" : 1,
    "b" : 0,
    "c" : 0,
    "d" : 0,
    "e" : 0,
    "f" : 0,
    "g" : 0,
    "h" : 0
}

pc = 0
muls = 0
runs = 0
while pc >= 0 and pc < len(instr):
    if(instr[pc][0] == "set"):
        if(isNumber(instr[pc][2])):
            value = int(instr[pc][2])
        else:
            value = regs[instr[pc][2]]
        regs[instr[pc][1]] = value
        pc += 1
    elif(instr[pc][0] == "sub"):
        if(isNumber(instr[pc][2])):
            value = int(instr[pc][2])
        else:
            value = regs[instr[pc][2]]
        regs[instr[pc][1]] = regs[instr[pc][1]] - value
        pc += 1
    elif(instr[pc][0] == "mul"):
        if(isNumber(instr[pc][2])):
            value = int(instr[pc][2])
        else:
            value = regs[instr[pc][2]]
        regs[instr[pc][1]] = regs[instr[pc][1]] * value
        muls += 1
        pc += 1
    elif(instr[pc][0] == "jnz"):
        if(isNumber(instr[pc][1])):
            jmp = int(instr[pc][1])
        else:
            jmp = regs[instr[pc][1]]
        if(jmp != 0):
            if(isNumber(instr[pc][2])):
                value = int(instr[pc][2])
            else:
                value = regs[instr[pc][2]]
            pc += value
        else:
            pc += 1

    runs += 1
    if(runs % 1000000000 == 0):
        print regs["h"]
print muls
print regs["h"]
