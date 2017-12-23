def circularBuffer(limit):
    buff = [0]
    next_insertion = 1
    steps = 386
    index = 0
    length = 1

    while(next_insertion <= limit):
        index = (index + steps) % length
        buff.insert(index + 1, next_insertion)
        next_insertion += 1
        index += 1
        length += 1

    return buff

def fastCircularBuffer(limit):
    next_insertion = 1
    steps = 386
    index = 0
    length = 1
    indexZero = 0
    afterZero = 0

    while(next_insertion <= limit):
        index = ((index + steps) % length) + 1
        if(index <= indexZero):
            indexZero += 1
        elif(index == indexZero + 1):
            afterZero = next_insertion

        next_insertion += 1
        length += 1

    return afterZero

t1 = circularBuffer(2017)
t2 = fastCircularBuffer(5 * (10**7))

print "Task 1 " + str(t1[t1.index(2017) + 1])
print "Task 2 " + str(t2)
