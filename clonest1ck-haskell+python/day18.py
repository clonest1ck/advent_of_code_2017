def fetchArg(prefix, arg, regs):
    if(not is_number(arg)):
        if(not regs.has_key(prefix + arg)):
            regs[prefix + arg] = 0
        return [regs[prefix + arg], regs]
    else:
        return [int(arg), regs]

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def task1():
    f = open("in18.txt", 'r')
    instructions = [x.split("\n")[0] for x in f.readlines()]

    regs = {}
    i = 0
    while(i < len(instructions)):
        instr = instructions[i].split(" ")
        instr[-1] = instr[-1].split("\r")[0]

        if(instr[0] == "snd"):
            [value, regs] = fetchArg("", instr[1], regs)
            regs["snd"] = value
        elif(instr[0] == "set"):
            [value, regs] = fetchArg("", instr[2], regs)
            regs[instr[1]] = value
        elif(instr[0] == "add"):
            [value, regs] = fetchArg("", instr[2], regs)
            if(not regs.has_key(instr[1])):
                regs[instr[1]] = 0
            regs[instr[1]] += value
        elif(instr[0] == "mul"):
            [value, regs] = fetchArg("", instr[2], regs)
            if(not regs.has_key(instr[1])):
                regs[instr[1]] = 0
            regs[instr[1]] =  regs[instr[1]] * value
        elif(instr[0] == "mod"):
            [value, regs] = fetchArg("", instr[2], regs)
            if(not regs.has_key(instr[1])):
                regs[instr[1]] = 0
            regs[instr[1]] = regs[instr[1]] % value
        elif(instr[0] == "rcv"):
            [value, regs] = fetchArg("", instr[1], regs)
            if(value != 0):
                [value, regs] = fetchArg("", "snd", regs)
                regs["rcv"] = value
                break
        elif(instr[0] == "jgz"):
            [value, regs] = fetchArg("", instr[1], regs)
            if(value > 0):
                [value, regs] = fetchArg("", instr[2], regs)
                i += value
                continue
        i += 1
    print "Task 1: " + str(regs["rcv"])


def task2():
    f = open("in18.txt", 'r')
    instructions = [x.split("\n")[0] for x in f.readlines()]

    regs = {
        "0_p"   : 0,
        "1_p"   : 1,
        "0_pc"  : 0,
        "1_pc"  : 0,
        "0_rec" : [],
        "1_rec" : [],
        "0_wai" : False,
        "1_wai" : False
    }
    i = 0
    prog = "0_"
    sent = 0
    while(i < len(instructions)):
        regs[prog + "wai"] = False
        instr = instructions[i].split(" ")
        instr[-1] = instr[-1].split("\r")[0]

        if(instr[0] == "snd"):
            [value, regs] = fetchArg(prog, instr[1], regs)
            if(prog == "0_"):
                to = "1_rec"
            else:
                to = "0_rec"
                sent += 1
            regs[to].append(value)
        elif(instr[0] == "set"):
            [value, regs] = fetchArg(prog, instr[2], regs)
            regs[prog + instr[1]] = value
        elif(instr[0] == "add"):
            [value, regs] = fetchArg(prog, instr[2], regs)
            if(not regs.has_key(prog + instr[1])):
                regs[prog + instr[1]] = 0
            regs[prog + instr[1]] += value
        elif(instr[0] == "mul"):
            [value, regs] = fetchArg(prog, instr[2], regs)
            if(not regs.has_key(prog + instr[1])):
                regs[prog + instr[1]] = 0
            regs[prog + instr[1]] =  regs[prog + instr[1]] * value
        elif(instr[0] == "mod"):
            [value, regs] = fetchArg(prog, instr[2], regs)
            if(not regs.has_key(prog + instr[1])):
                regs[prog + instr[1]] = 0
            regs[prog + instr[1]] = regs[prog + instr[1]] % value
        elif(instr[0] == "rcv"):
            if(len(regs[prog + "rec"]) == 0):
                regs[prog + "pc"] = i
                regs[prog + "wai"] = True
                if(prog == "0_"):
                    prog = "1_"
                else:
                    prog = "0_"
                i = regs[prog + "pc"]
                if(regs["0_wai"] and regs["1_wai"] and len(regs["0_rec"]) == 0 and len(regs["1_rec"]) == 0):
                    break
                continue
            else:
                regs[prog + instr[1]] = regs[prog + "rec"].pop()
        elif(instr[0] == "jgz"):
            [value, regs] = fetchArg(prog, instr[1], regs)
            if(value > 0):
                [value, regs] = fetchArg(prog, instr[2], regs)
                i += value
                continue
        i += 1
        if(not i < len(instructions)):
            if progs["0_wai"]:
                prog = "0_"
            elif progs["1_wai"]:
                prog = "1_"
            i = progs[prog + "pc"]

    print "Task 2: " + str(sent)

task1()
task2()
