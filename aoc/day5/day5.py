import queue

def main():
    q1 = queue.LifoQueue()
    q2 = queue.LifoQueue()
    q3 = queue.LifoQueue()
    q4 = queue.LifoQueue()
    q5 = queue.LifoQueue()
    q6 = queue.LifoQueue()
    q7 = queue.LifoQueue()
    q8 = queue.LifoQueue()
    q9 = queue.LifoQueue()
    swap = queue.LifoQueue()
    listq = [q1, q2, q3, q4, q5, q6, q7, q8, q9]

    with open("day5\\input2.txt") as f:
        for line in f:
            line = line.strip().split(",")
            for x in range(len(line)):
                if len(line[x]) > 1:
                    listq[x].put(line[x])
        
    with open("day5\\input.txt") as f:
        for line in f:
            line = line.strip().split()
            for x in range(int(line[1])):
                swap.put(listq[int(line[3])-1].get())
            for x in range(int(line[1])):
                listq[int(line[-1])-1].put(swap.get())
    for x in listq:
        print(x.get(),end='')

main()